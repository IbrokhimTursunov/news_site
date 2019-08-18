$(document).ready(
    function() {
        $("#search_button").click(
            function() {
                send_search('search_form', 'search-news');
                return false;
            }
        );
        get_news('news');
    }
)

function send_search(form_id, url) {
    $.ajax({
        url: url,
        type: "GET",
        dataType: "json",
        data: $("#"+form_id).serialize(),
        success: function(response) {
            clear_news("news");
            populate_news("news", response);
        }
    });
}

function get_news(url) {
    $.ajax({
        url: url,
        type: "GET",
        dataType: "json",
        success: function(response) {
            console.log(response)
            populate_news("news", response);
        }
    });
}

function clear_news(div_id) {
    $("#" + div_id).html('')
}

function populate_news(div_id, data) {
    if (data.length > 0) {
        for (let item of data) {
            let title = '<div class="container title">' + item.title + '</div>';
            $("#" + div_id).append(title);
            let content = '<div class="container content">' + item.content + '</div>';
            $("#" + div_id).append(content);
        }
    } else {
        $("#" + div_id).append("Ничего не найдено.");
    }
}

function pupulate_news_with_initial_data(div_id) {

}
