const scrollShow = () => {
  let pageTop = $(document).scrollTop();
  let pageBottom = pageTop + $(window).height();

  for (let tag of $('.container')) {
    if ($(tag).position().top < pageBottom) {
      $(tag).addClass("visible");
    } else {
      $(tag).removeClass("visible");
    }
  }
}

$(document).on("DOMContentLoaded", () => {
  $(document).on("scroll", scrollShow);
  scrollShow();
})
