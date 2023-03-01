function translate_text() {
    var data = $('#data').val();
    var lang = $('#lang').val();
    $.ajax({
        url: "http://localhost:3001/translate_text",
        type: "POST",
        data: {data: data, lang: lang},
        crossDomain: true,
        success: function(response) {
            console.log(response);
            var html = "<br><br><br><p> <b> RESULT : </b><p>";
            $.each(response, function(key,val){
                console.log(val);
                html+="<p>"+val+"</p>"
            });
            html +="<br>";
            $(".show-data").empty().append(html);
        },
        error: function(xhr, status, error) {
            console.log(xhr.responseText);
        }
    });
};

function translate_img() {
    var file = document.getElementById('file').files[0]['name'];
    var lang = $('#lang').val();
    console.log(file);
    var formData = new FormData();
	formData.append('file', file);
    formData.append('lang', lang);
    console.log(formData);
    $.ajax({
        url: 'http://localhost:3001/translate_img',
        type: 'POST',
        data: formData,
        processData: false,
        contentType: false,
        crossDomain: true,
        success: function(response) {
            console.log(response);
            var html = "<br><br><br><p> <b> RESULT : </b><p>";
            $.each(response, function(key,val){
                console.log(val);
                html+="<p>"+val+"</p>"
            });
            html +="<br>";
            $(".show-data").empty().append(html);
        },
        error: function(xhr, status, error) {
            console.error(xhr.responseText);
        }
    });
};