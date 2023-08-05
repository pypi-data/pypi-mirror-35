import re
import email
import base64
import hashlib
from HTMLParser import HTMLParser
from swimbundle_email import EmailParser, EmailUtil, EmailAttachmentList, EmailAttachment


class EMLParser(EmailParser):
    def __init__(self, filename, email_data):
        super(EMLParser, self).__init__(filename, email_data)
        self.msg = email.message_from_string(base64.b64decode(email_data))

    def get_sender(self):
        return EmailUtil.try_decode(self.msg['From']) or u""

    def get_reply_to(self):
        return EmailUtil.try_decode(self.msg["Reply-To"]) or u""

    def get_plaintext_body(self):
        if self.msg.is_multipart():
            for part in self.msg.walk():
                ctype = part.get_content_type()
                cdispo = str(part.get('Content-Disposition'))
                if ctype == 'text/plain' and 'attachment' not in cdispo:
                    return part.get_payload(decode=True).decode("utf-8", errors="replace")
        else:
            if self.msg.get_content_type() == "text/plain":
                return self.msg.get_payload(decode=True).decode("utf-8", errors="replace")

        return u""

    def get_html_body(self, decode_html=True):
        if self.msg.is_multipart():
            for part in self.msg.walk():
                ctype = part.get_content_type()
                cdispo = str(part.get('Content-Disposition'))
                if ctype == 'text/html' and 'attachment' not in cdispo:
                    # Try decoding HTML Entities
                    body = part.get_payload(decode=True).decode('utf8', errors="replace")
                    if decode_html:
                        return HTMLParser().unescape(body) or u""
                    else:
                        return body or u""
        else:
            if self.msg.get_content_type() == "text/html":
                return self.msg.get_payload(decode=True).decode("utf-8", errors="replace")

        return u""

    def get_rtf_body(self):
        return u""  # Pretty sure EML files can't/shouldn't have rtf bodies

    def get_subject(self):
        return EmailUtil.try_decode(self.msg['Subject']) if self.msg['Subject'] else "(No Subject)"

    def get_type(self):
        return "EML"

    def get_date(self):
        return self.msg['Date'] or ""

    def get_recipients(self):
        return EmailUtil.try_decode(self.msg['To']) or ""

    def get_id(self):
        return self.msg['id'] or self.msg['Message-ID'] or ""

    def get_headers(self):
        parser = email.parser.HeaderParser()
        headers = parser.parsestr(self.msg.as_string()).items()
        return headers if headers else []

    def get_attachments(self):
        """
        Handle the attachments and return strings of 'attachments_md5', 'attachments_sha1' and 'attach_info', the hashed
        data of the attachments, where attach_info is the Content-Type and Content-Transfer-Encoding concatenated
        :return: dictionary with csv values
        """
        raw_attachments = self._organize_attachments(self.msg)
        attachments = EmailAttachmentList()

        for raw_attachment in raw_attachments:
            filename = self._get_attachment_filename(raw_attachment[0], hashlib.md5(raw_attachment[1]).hexdigest())
            email_attachment = EmailAttachment(
                " ".join(["{}: {}".format(k, v) for k, v in raw_attachment[0].iteritems()]),
                filename, raw_attachment[1])

            # Make sure that the attachments aren't the same as the html_body or plaintext_body
            email_attachment.raw_data = email_attachment.raw_data.decode("utf-8", errors="replace")
            bodies = (self.get_html_body(decode_html=False), self.get_plaintext_body(), self.get_rtf_body())
            if email_attachment.raw_data not in bodies:
                attachments.add_attachment(email_attachment)

        return attachments.to_swimlane_output()


    @staticmethod
    def _get_attachment_filename(attachment_headers, fallback_name):
        """
        Attempt to get the filename from the content-type information, otherwise just use the fallback name
        :param attachment_headers: List of headers for the attachment
        :param fallback_name: Name to use if we can't find a filename, will be prefixed with unknown-<name>
        :return: filename to use for the attachment
        """
        filename = "unknown-{}".format(fallback_name)
        if "content-location" in attachment_headers:
            filename = attachment_headers["content-location"]
        elif "content-type" in attachment_headers:
            properties = attachment_headers["content-type"].split(";")
            for prop in properties:
                prop = prop.strip()  # Strip \t from prop
                if prop.startswith("name") or prop.startswith("filename"):
                    # Split 'name="asdf.png"' into 'asdf.png'
                    filename = re.split("name=\"?", prop)
                    if len(filename) > 1:  # If split failed we can't determine filename
                        filename = filename[1]
                        if filename.endswith("\"") or filename.endswith("\'"):
                            filename = filename[:-1]  # Cut off trailing quote
                    break

        return EmailUtil.try_decode(filename)  # Try and decode filenames that are encoded with mime encoded-word syntax

    @staticmethod
    def _is_attachment(headers):
        """
        Check if a given payload is an attachment (or it's email body)
        Valid from https://www.w3.org/Protocols/rfc1341/5_Content-Transfer-Encoding.html
        :param headers:
        :return:
        """
        if "content-disposition" in headers:
            if headers["content-disposition"].startswith("attachment"):
                return True
        if "content-transfer-encoding" in headers:
            trans_enc = headers["content-transfer-encoding"].lower()
            if trans_enc in ("quoted-printable", "7bit", "8bit"):
                return False
            else:
                return True

    def _organize_attachments(self, eml_obj):
        """
        Organize and filter the attachment data
        :param eml_obj: email object to organize
        :return: List like [[headers, attachment], ...]
        """
        data = []
        for attachment in list(eml_obj.walk()):
            if attachment.is_multipart():
                continue  # Ignore multipart, since .walk() finds everything for you
            else:
                newdata = self._decode_payload(attachment)  # Actual data of the file
                headers = {}
                for k, v in attachment.items():
                    headers[k.lower()] = v
                if self._is_attachment(headers):
                    data.append([headers, newdata])
        return data

    @staticmethod
    def _decode_payload(attachment):
        """
        Take a given email payload and get the raw unencoded data
        :param attachment: email attachment part
        :return:
        """
        data = attachment.get_payload()
        if "content-transfer-encoding" in attachment:
            if attachment["Content-Transfer-Encoding"] == "base64":
                data = base64.b64decode(data)
        return data
