import youtube_dl as ytdl
import discord

ytdl_options = {
    'format': 'bestaudio/best',
    'restrictfilenames': True,
    'noplaylist': True,
    'nocheckcertificate': True,
    'quiet': True,
    'ignoreerrors': False,
    'logtostderr': False,
    'no_warnings': True,
    'default_search': 'auto',
    'source_address': '0.0.0.0'
}


class Video:
    """Class containing information about a particular video."""

    def __init__(self, url_or_search, requested_by):
        """Plays audio from (or searches for) a URL."""
        with ytdl.YoutubeDL(ytdl_options) as ydl:
            info_dict = ydl.extract_info(url_or_search, download=False)
            self.stream_url = video_format['entries'][0]["url"]
            self.video_url = info_dict["webpage_url"]
            self.title = info_dict['entries'][0]['title']
            self.uploader = info_dict['entries'][0]["uploader"] if "uploader" in info_dict['entries'][0] else ""
            self.thumbnail = info_dict['entries'][0]["thumbnail"] if "thumbnail" in info_dict['entries'][0] else None
            self.requested_by = requested_by

    def get_embed(self):
        """Makes an embed out of this Video's information."""
        embed = discord.Embed(
            title=self.title, description=self.uploader, url=self.video_url)
        embed.set_footer(
            text=f"Requested by {self.requested_by.name}",
            icon_url=self.requested_by.avatar_url)
        if self.thumbnail:
            embed.set_thumbnail(url=self.thumbnail)
        return embed

