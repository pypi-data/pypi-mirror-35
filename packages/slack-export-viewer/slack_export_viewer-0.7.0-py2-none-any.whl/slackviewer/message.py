from __future__ import unicode_literals

import datetime
import logging
import re

import emoji
import markdown2


class Message(object):

    _DEFAULT_USER_ICON_SIZE = 72

    def __init__(self, USER_DATA, CHANNEL_DATA, message):
        self.__USER_DATA = USER_DATA
        self.__CHANNEL_DATA = CHANNEL_DATA
        self._message = message

    ##############
    # Properties #
    ##############

    @property
    def user_id(self):
        return self._message["user"]

    @property
    def user(self):
        return self.__USER_DATA[self.user_id]

    @property
    def username(self):
        try:
            return self.user.display_name
        except KeyError:
            # In case this is a bot or something, we fallback to "username"
            if "username" in self._message:
                return self._message["username"]
            # If that fails to, it's probably USLACKBOT...
            if "user" in self._message:
                if self.user_id == "USLACKBOT":
                    return "slackbot"
                else:
                    return self.user_id
            elif "bot_id" in self._message:
                return self._message["bot_id"]
            else:
                return None

    @property
    def time(self):
        # Handle this: "ts": "1456427378.000002"
        tsepoch = float(self._message["ts"].split(".")[0])
        return str(datetime.datetime.fromtimestamp(tsepoch)).split('.')[0]

    @property
    def msg(self):
        message = []

        text = self._message.get("text")
        if text:
            text = self._render_text(text)
            message.append(text)

        attachments = self._message.get("attachments", [])
        if attachments is not None:
            for att in attachments:
                message.append("")
                if "pretext" in att:
                    pretext = self._render_text(att["pretext"].strip())
                    message.append(pretext)
                if "title" in att:
                    title = self._render_text("**{}**".format(
                        att["title"].strip()
                    ))
                    message.append(title)
                if "text" in att:
                    text = self._render_text(att["text"].strip())
                    message.append(text)

        file_link = self._message.get("file", {})
        # We would like to show file if it is image type
        if (
            file_link and
            "url_private" in file_link and
            "mimetype" in file_link and
            file_link["mimetype"].split('/')[0] == 'image'
        ):
            html = "<br><a href=\"{url}\"><img src=\"{url}\" height=\"200\"></a><br>" \
                .format(url=file_link["url_private"])
            message.append(html)

        if message:
            if not message[0].strip():
                message = message[1:]
        return "<br />".join(message).strip()

    @property
    def img(self):
        try:
            return self.user.image_url(self._DEFAULT_USER_ICON_SIZE)
        except KeyError:
            return ""

    @property
    def id(self):
        return self.time

    @property
    def subtype(self):
        return self._message.get("subtype")

    ###################
    # Private Methods #
    ###################

    def _render_text(self, message):
        message = message.replace("<!channel>", "@channel")
        message = self._slack_to_accepted_emoji(message)
        # Handle "<@U0BM1CGQY|calvinchanubc> has joined the channel"
        message = re.sub(r"<@U\w+\|[A-Za-z0-9.-_]+>",
                         self._sub_annotated_mention, message)
        # Handle "<@U0BM1CGQY>"
        message = re.sub(r"<@U\w+>", self._sub_mention, message)
        # Handle links
        message = re.sub(
            # http://stackoverflow.com/a/1547940/1798683
            # TODO This regex is likely still incomplete or could be improved
            r"<(https|http|mailto):[A-Za-z0-9_\.\-\/\|\?\,\=\#\:\@]+>",
            self._sub_hyperlink, message
        )
        # Handle hashtags (that are meant to be hashtags and not headings)
        message = re.sub(r"(^| )#[A-Za-z0-9\.\-\_]+( |$)",
                         self._sub_hashtag, message)
        # Handle channel references
        message = re.sub(r"<#C0\w+>", self._sub_channel_ref, message)
        # Handle italics (convert * * to ** **)
        message = re.sub(r"(^| )\*[A-Za-z0-9\-._ ]+\*( |$)",
                         self._sub_bold, message)
        # Handle italics (convert _ _ to * *)
        message = re.sub(r"(^| )_[A-Za-z0-9\-._ ]+_( |$)",
                         self._sub_italics, message)

        # Escape any remaining hash characters to save them from being turned
        #  into headers by markdown2
        message = message.replace("#", "\\#")

        message = markdown2.markdown(
            message,
            extras=[
                "cuddled-lists",
                # Disable parsing _ and __ for em and strong
                # This prevents breaking of emoji codes like :stuck_out_tongue
                #  for which the underscores it liked to mangle.
                # We still have nice bold and italics formatting though
                #  because we pre-process underscores into asterisks. :)
                "code-friendly",
                # This gives us <pre> and <code> tags for ```-fenced blocks
                "fenced-code-blocks",
                "pyshell"
            ]
        ).strip()

        # Newlines to breaks
        # Special handling cases for lists
        message = message.replace("\n\n<ul>", "<ul>")
        message = message.replace("\n<li>", "<li>")

        # Introduce unicode emoji
        message = emoji.emojize(message, use_aliases=True)

        return message

    def _slack_to_accepted_emoji(self, message):
        # https://github.com/Ranks/emojione/issues/114
        message = message.replace(":simple_smile:", ":slightly_smiling_face:")
        return message

    def _sub_mention(self, matchobj):
        try:
            return "@{}".format(
                self.__USER_DATA[matchobj.group(0)[2:-1]].display_name
            )
        except KeyError:
            # In case this identifier is not in __USER_DATA, we fallback to identifier
            return matchobj.group(0)[2:-1]

    def _sub_annotated_mention(self, matchobj):
        return "@{}".format((matchobj.group(0)[2:-1]).split("|")[1])

    def _sub_hyperlink(self, matchobj):
        compound = matchobj.group(0)[1:-1]
        if len(compound.split("|")) == 2:
            url, title = compound.split("|")
        else:
            url, title = compound, compound
        result = "[{title}]({url})".format(url=url, title=title)
        return result

    def _sub_hashtag(self, matchobj):
        text = matchobj.group(0)

        starting_space = " " if text[0] == " " else ""
        ending_space = " " if text[-1] == " " else ""

        return "{}*{}*{}".format(
            starting_space,
            text.strip(),
            ending_space
        )

    def _sub_channel_ref(self, matchobj):
        channel_id = matchobj.group(0)[2:-1]
        try:
            channel_name = self.__CHANNEL_DATA[channel_id]["name"]
        except KeyError as e:
            logging.error("A channel reference was detected but metadata "
                          "not found in channels.json: {}".format(e))
            channel_name = channel_id
        return "*#{}*".format(channel_name)

    def __em_strong(self, matchobj, format="em"):
        if format not in ("em", "strong"):
            raise ValueError
        chars = "*" if format == "em" else "**"

        text = matchobj.group(0)
        starting_space = " " if text[0] == " " else ""
        ending_space = " " if text[-1] == " " else ""
        return "{}{}{}{}{}".format(
            starting_space,
            chars,
            matchobj.group(0).strip()[1:-1],
            chars,
            ending_space
        )

    def _sub_italics(self, matchobj):
        return self.__em_strong(matchobj, "em")

    def _sub_bold(self, matchobj):
        return self.__em_strong(matchobj, "strong")
