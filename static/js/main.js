$(document).ready(function() {
    $('#btnAnalysis').click(function() {
        text = $('#txtInput').val()
        data = JSON.stringify(text);
        if(text.length > 0) {

            // $.ajax({
            //     type : 'POST',
            //     url : '{{url_for(\'result\')}}',
            //     contentType: 'application/json;charset=UTF-8',
            //     data : {'text':text}, 
            //     success : function(data) {
            //         $('#spanResult').html(data)
            //     }
            //   });

            $.post('/result',data,function(res) {
                $('#spanResult').html(res)
            })

        }else{
            alert('Vui lòng nhập câu cần phân tích !')
        }
    })
})
