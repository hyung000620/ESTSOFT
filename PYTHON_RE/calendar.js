$(document).ready(function(){
	calendarInit();
	$("#sdate,#edate,#rdate").datepicker({changeMonth:true,changeYear:true,showButtonPanel:true});	
	$("#btnSubmit").click(function(){fm_check();});
	if($('#edu_id').val()!="" && $('#edu_teacher').val()!=""){
        $('#sel_teacher').val($('#edu_teacher').val()+"|"+$('#edu_id').val()).attr('selected','selected');
    }
    $('#sel_teacher').on('change', function(){
        let name = $(this).val().split("|")[0];
        let tid = $(this).val().split("|")[1];
        $('#edu_id').val(tid);
        $('#edu_teacher').val(name);
        $('#edu_id').attr('readonly',true);
        $('#edu_teacher').attr('readonly',true);
        if($(this).val()==0){
            $('#edu_teacher').val("");
            $('#edu_id').attr('readonly',false);
            $('#edu_teacher').attr('readonly',false);    
        }
	});
	$('#edate, #sdate, #rdate').on('change', function(){calendarInit();});
});
function link_view()
{
	var link_url="";
	link_url=$("#edu_addr").val();
	if(link_url=="")
	{alert("링크 주소를 입력 해 주세요.");return;}
	window.open("http://map.daum.net/?q="+link_url);
}

function link_view2()
{
	var link_view2="";
	link_view2=$("#link").val();
	
	if(link_view2=="")
{alert("링크 주소를 입력 해 주세요.");return;}
	
	window.open(link_view2);
}
function fm_check()
{
	if($("#edu_title").val()=="")
	{
		alert("교재제목 입력하세요.");
		return;
	}
	$("#fm").submit();
}
//calendar
function calendarInit() 
{
	let arr_day = [];
    let wrap = [];
	let arr_yoil=['일','월','화','수','목','금','토'];
    wrap.push("<div class=\"sec_cal\">");
    wrap.push("<div class=\"cal_nav\">")
    wrap.push("<a href=\"javascript:;\" class=\"nav-btn go-prev\"></a>");
    wrap.push("<div class=\"year-month\"></div>");
    wrap.push("<a href=\"javascript:;\" class=\"nav-btn go-next\"></a></div>");
    wrap.push("<div class=\"cal_wrap\"><div class=\"days\">");
    wrap.push("<div class=\"day\">일</div>");
    wrap.push("<div class=\"day\">월</div>");
    wrap.push("<div class=\"day\">화</div>");
    wrap.push("<div class=\"day\">수</div>");
    wrap.push("<div class=\"day\">목</div>");
    wrap.push("<div class=\"day\">금</div>");
    wrap.push("<div class=\"day\">토</div></div><div class=\"dates\"></div></div></div>");
    $('#cal').html(wrap.join(""));
    // 날짜 정보 가져오기
    let date = new Date(); // 현재 날짜(로컬 기준) 가져오기
    let utc = date.getTime() + (date.getTimezoneOffset() * 60 * 1000); // uct 표준시 도출
    let kstGap = 9 * 60 * 60 * 1000; // 한국 kst 기준시간 더하기
    let today = new Date(utc + kstGap); // 한국 시간으로 date 객체 만들기(오늘)
	let thisMonth;
	
	if($('#sdate').val()==""){thisMonth= new Date(today.getFullYear(), today.getMonth(), today.getDate());}
	else{thisMonth= new Date($('#sdate').val());}
	
    //설정한 기간
	let sdate = getDate($('#sdate').val());
	let edate = getDate($('#edate').val());
	let rdate = getDate($('#rdate').val());
    

    // 달력에서 표기하는 날짜 객체
    let currentYear = thisMonth.getFullYear(); // 달력에서 표기하는 연
    let currentMonth = thisMonth.getMonth(); // 달력에서 표기하는 월
    let currentDate = thisMonth.getDate(); // 달력에서 표기하는 일
	let urlParams = new URLSearchParams(window.location.search); //현재 url params
	if(urlParams.has('idx')){renderCalender_ajax(thisMonth,sdate,edate);}
	else{renderCalender(thisMonth,sdate,edate);}

	


	//등록
    function renderCalender(thisMonth,sdate,edate) 
    {
		let calendar = [];
		// 렌더링을 위한 데이터 정리
		currentYear = thisMonth.getFullYear();
		currentMonth = thisMonth.getMonth();
		currentDate = thisMonth.getDate();
		
		makeCalendar(currentYear, currentMonth,calendar,sdate,edate);
		
		$('.dates .current').click(function(){
			if($('#sdate').val()==""){alert("시작 일자를 입력해주세요."); return;}
			if($('#edate').val()==""){alert("종료 일자를 입력해주세요."); return;}
			let mon = currentMonth+1;
			let day = $(this).text();
            let cday = new Date(currentYear,mon,day);
            if(cday<sdate || cday>edate){alert('일정에서 벗어났습니다. 다시 시도해주세요.'); return;}
			
            if(mon<10){mon="0"+mon;}
			if(day<10){day="0"+day;}
			let val = currentYear+"-"+mon+"-"+day;
			if($(this).hasClass('today')){$(this).removeClass('today');for(let i=0; i< arr_day.length; i++){if(arr_day[i]== val){arr_day.splice(i, 1);i--;}}}
            else{arr_day.push(val);$(this).addClass('today');}
			$('#open_date').val(arr_day.join("|"));
            
		});
		
    }
    //수정
	function renderCalender_ajax(thisMonth,sdate,edate)
	{
		let calendar = [];
		$.ajax(
		{
			type:"POST",
			url: "/SuperAdmin/xml/edu_write.php",
			data: $('#fm').serialize(),
			dataType: "JSON",
			success:function(data){		
				currentYear = thisMonth.getFullYear();
				currentMonth = thisMonth.getMonth();
				currentDate = thisMonth.getDate();
                makeCalendar(currentYear, currentMonth,calendar,sdate,edate);
				$.each(data.open_date, function(idx,val){
					for(let i=0; i< arr_day.length; i++){if(arr_day[i]== val){arr_day.splice(i, 1);i--;}}
					arr_day.push(val);
				});

				$('.dates .current').click(function(){
					let mon = currentMonth+1;
					let day = $(this).text();
					if(mon<10){mon="0"+mon;}
					if(day<10){day="0"+day;}
					let val = currentYear+"-"+mon+"-"+day;
					if($(this).hasClass('today')){$(this).removeClass('today');for(let i=0; i< arr_day.length; i++){if(arr_day[i]== val){arr_day.splice(i, 1);i--;}}}
                    else{arr_day.push(val);$(this).addClass('today');}
					$('#open_date').val(arr_day.join("|"));
				});
                
				reloadCalendar();
			}
		});
		
	}
	
    // 이전달로 이동
    $('.go-prev').on('click', function() {
		thisMonth = new Date(currentYear, currentMonth - 1, 1);
        if(sdate.getMonth()==(currentMonth+1)){alert('설정하신 일정에서 벗어났습니다. 다시 시도해주세요'); return;}
        if(urlParams.has('idx')){renderCalender_ajax(thisMonth,sdate,edate);}
		else{renderCalender(thisMonth,sdate,edate);}
		reloadCalendar();
    });
	
    // 다음달로 이동
    $('.go-next').on('click', function() {
		thisMonth = new Date(currentYear, currentMonth + 1, 1);
        if(edate.getMonth()==thisMonth.getMonth()){alert('설정하신 일정에서 벗어났습니다. 다시 시도해주세요'); return;}
        if(urlParams.has('idx')){renderCalender_ajax(thisMonth,sdate,edate);}
		else{renderCalender(thisMonth,sdate,edate);}
		reloadCalendar();
    });
    
    //데이터에 해당되는 달력에 마킹
	function reloadCalendar()
	{
        arr_day = $('#open_date').val().split("|");
		$.each(arr_day, function(idx, val){
			let d = new Date(val);
			if(d.getMonth()==currentMonth && d.getFullYear() == currentYear)
			{
				$(`.dates .current:eq(${d.getDate() -1})`).addClass("today");
			}
		});
        //오늘 날짜 표기
        if (today.getMonth() == currentMonth) {
            $(`.dates .current:eq(${today.getDate() -1})`).addClass('select');
        }
		//접수 날짜 표기
        if (rdate.getMonth() == (currentMonth-1)) {
            $(`.dates .current:eq(${rdate.getDate() -1})`).addClass('rdate');
        }
	}

    //기본 달력 불러오기
    function makeCalendar(currentYear, currentMonth,calendar,sdate, edate)
    {
        //이전 달의 마지막 날 날자와 요일 구하기
        let startDay = new Date(currentYear, currentMonth, 0);
        let prevDate = startDay.getDate();
        let prevDay = startDay.getDay();
        //이번 달의 마지막 날 날짜와 요일 구하기
        let endDay = new Date(currentYear, currentMonth + 1, 0);
        let nextDate = endDay.getDate();
        let nextDay = endDay.getDay();
        //현재 월 표기
        $('.year-month').text(currentYear + '.' + (currentMonth + 1));
        //렌더링 html 요소 생성
        //지난달
        for (let i = prevDate - prevDay; i <= prevDate; i++) {
            calendar.push("<div class=\"day prev disable\">" + i + "</div>");
        }
        //이번달
        if(prevDay == 6){calendar=[];}
        for (let i = 1; i <= nextDate; i++) {
            calendar.push("<div class=\"day current disable\">" + i + "</div>");
        }
        //다음달
        for (let i = 1; i <= (7 - nextDay == 7 ? 6 : 6 - nextDay); i++) {
            calendar.push("<div class=\"day next disable\">" + i + "</div>")
        }
        $('.dates .current').off('click');
        $('.dates').html(calendar.join(""));
        //오늘 날짜 표기
        if (today.getMonth() == currentMonth) {
            $(`.dates .current:eq(${today.getDate() -1})`).addClass('select');
        }
        //기간 설정한 날짜 활성화
        $('.dates .current').each(function(){
            if(sdate.getMonth()==edate.getMonth()){
                if($(this).text()>=sdate.getDate()&& $(this).text()<=edate.getDate()){
                    $(this).removeClass('disable');
                    $(this).addClass('bold');
                }
            }else{
				let cmonth = currentMonth+1;
                if(sdate.getMonth()==cmonth && $(this).text()>=sdate.getDate() ){
                    $(this).removeClass('disable');
                    $(this).addClass('bold');
                }else if(edate.getMonth()==cmonth && $(this).text()<=edate.getDate()){
					$(this).removeClass('disable');
                    $(this).addClass('bold');
                }else if(sdate.getMonth()<cmonth && edate.getMonth()>cmonth){
					$(this).removeClass('disable');
                    $(this).addClass('bold');
				}
            }
        });
		//접수 날짜 표기
		if (rdate.getMonth()-1 == currentMonth) {
			$(`.dates .current:eq(${rdate.getDate() -1})`).addClass('rdate');
		}
    }
	

    //요일에 해당하는 데이터 전부 클릭
	$('.days .day').on('click',function(){
		let sel_yoil=arr_yoil.indexOf($(this).text());
		$('.dates .current').each(function(){
			if($(this).hasClass('disable')==false){
				thisMonth = new Date(currentYear, currentMonth, $(this).text());
				if($(this).hasClass('today')){
					//$(this).removeClass('today');for(let i=0; i< arr_day.length; i++){if(arr_day[i]== val){arr_day.splice(i, 1);i--;}}
				}else{
					if(thisMonth.getDay()==sel_yoil){
						console.log($(this).text());
						let mon = thisMonth.getMonth()+1;
						let day = thisMonth.getDate();
						if(mon<10){mon="0"+mon;}
						if(day<10){day="0"+day;}
						arr_day.push(thisMonth.getFullYear()+"-"+mon+"-"+day);
					};
				}
			}
		});
		$('#open_date').val(arr_day.join("|"));
		reloadCalendar();
	});

	//날짜값
	function getDate(str)
	{
		let year = parseInt(str.split('-')[0]);
		let month = parseInt(str.split('-')[1]);
		let date = parseInt(str.split('-')[2]);
		return new Date(year, month, date);
	}
}