$(()=>{
    $('#changeTextBtn').click(()=>{
        $('#myHeading').text('안녕하세요');
    });
    
    $('#changeColorBtn').click(()=>{
        $('#myHeading').css('background-color','blue');
    });
    
    $('#addClassBtn').click(()=>{
        $('#myHeading').addClass('highlight');
        $('.highlight').css('color','yellow');
    });
    
    $('#removeClassBtn').click(()=>{
        $('#myHeading').removeClass('highlight');
    });

    $('#hideBtn').click(()=>{
        $("#myHeading").hide();
    });

    $('#showBtn').click(()=>{
        $("#myHeading").show();
    });
});

