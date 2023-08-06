import lxml
import requests
import lxml.html

from feed_to_exporter.model import AbstractFeedInfo
from feed_to_exporter.helpers import clean_html, MatchKeywords
from feed_to_exporter.exceptions import FeedToWordpressNotValidInfoFound


GENERAL_TAG = ("justicia-general", "Justicia Informacion General")


def feed_source_filter(field_value: str) -> dict:
    return {"feed_source": "Blog Adams Justicia"}


def global_filter(feed_info: AbstractFeedInfo) -> \
        dict or FeedToWordpressNotValidInfoFound:
    """
        This filter get Adams Post link and:
        1 - Download the content
        2 - Extract post content info
        3 - Analyze and try to find the correct tags for the post
        """
    #
    # Get remote post info
    #
    html_content = requests.get(feed_info.link).content
    parsed_content = lxml.html.fromstring(html_content)

    #
    # Split important info
    #
    content = clean_html(lxml.etree.tostring(
        parsed_content.xpath(".//*[@class='entry-area']")[0]
    ))
    content_lower_case = content.lower().decode("utf-8")

    post_key_words = [
        x.text.lower()
        for x in parsed_content.xpath(".//*[@class='meta cat-links']/a")
    ]

    # -------------------------------------------------------------------------
    # Try to find tags
    # -------------------------------------------------------------------------
    matcher = MatchKeywords(MatchKeywords.resolve_keywords_file(
        __file__,
        "../keywords.json"
    ))

    for tag_name, tag_description in matcher.match_entries((
            content_lower_case,
            post_key_words,
            feed_info.title
    )):
        try:
            feed_info.add_tag(tag_name,
                              tag_description)

        except AttributeError:
            print(tag_name)
            pass

    if not matcher.matches_found:
        feed_info.add_tag(*GENERAL_TAG)

    feed_info.active_categories_and_tags_in_wordpress()

    return {
        'body': content.decode("utf-8")
    }


INDIVIDUAL_VALIDATORS = {
    'feed_source': feed_source_filter
}

GLOBAL_VALIDATOR = global_filter

# if __name__ == '__main__':
    # f = FeedInfo(None,
    #              None,
    #              title="TRAMITACIÓN PROCESAL (P. INTERNA): PRESENTACIÓN DE DOCUMENTACIÓN",
    #              feed_source="http://www.adams.es/blogs/justicia/2018/08/tramitacion-procesal-p-interna-presentacion-de-documentacion/")
    # f.link = f.feed_source
    # global_filter(f)
