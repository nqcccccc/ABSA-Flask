$(document).ready(function() {
    $('#btnAnalysis').click(function() {
        text = $('#txtInput').val()
        data = JSON.stringify(text);
        if(text.length > 0) {
            let startTime = performance.now()

            $.post('/result',{text:text},function(res) {
                $('#spanResult').html(res)
                let endTime = performance.now()
                console.log(`Call to doSomething took ${endTime - startTime} milliseconds`)
            })
                
            
        }else{
            alert('Vui lòng nhập câu cần phân tích !')
        }
    })
})
