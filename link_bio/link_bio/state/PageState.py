from enum import Flag
import reflex as rx
import link_bio.utils as utils
from link_bio.api.api import live, featured, schedule
from link_bio.model.Featured import Featured
from link_bio.model.Live import Live

USER = "mouredev"


class PageState(rx.State):

    live_status = Live(live=False, title="")
    next_live: str = ""
    featured_info: list[Featured]

    async def check_live(self):
        self.live_status = await live(USER)
        if not self.live_status.live:
            await schedule()
            self.next_live = "Next"  # utils.next_date()

    async def featured_links(self):
        self.featured_info = await featured()
