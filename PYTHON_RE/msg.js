// 체크인 및 체크아웃 날짜 업데이트 함수
function updateDate(elementId, date) {
    document.getElementById(elementId).textContent = date;
}

// 모달 표시 함수
function showModal(modalId) {
    const modal = document.getElementById(modalId);
    modal.style.display = 'block';
}

// 모달 닫기 함수
function closeModal(modalId) {
    const modal = document.getElementById(modalId);
    modal.style.display = 'none';
}

// 체크인 텍스트 클릭 시 모달 표시
document.getElementById('checkin').addEventListener('click', function () {
    showModal('checkinModal');
});

// 체크인 모달 닫기 버튼 클릭 시 모달 닫기
document.getElementById('checkinClose').addEventListener('click', function () {
    closeModal('checkinModal');
});

document.getElementById('check').addEventListener('click', function () {
    const selectedDaysin = document.querySelectorAll('.selected-checkin');
    for (const selectedDay of selectedDaysin) {
        selectedDay.classList.remove('selected-checkin');
    }
    const selectedDaysout = document.querySelectorAll('.selected-checkout');
    for (const selectedDay of selectedDaysout) {
        selectedDay.classList.remove('selected-checkout');
    }
    selectedCheckinDate = null;
    selectedCheckoutDate = null;
});


// 선택된 날짜에 클래스 부여 함수
function selectCheckin(dayElem) {
    const selectedDays = document.querySelectorAll('.selected-checkin');
    for (const selectedDay of selectedDays) {
        selectedDay.classList.remove('selected-checkin');
    }
    dayElem.classList.add('selected-checkin');
}
function selectCheckout(dayElem) {
    const selectedDays = document.querySelectorAll('.selected-checkout');
    for (const selectedDay of selectedDays) {
        selectedDay.classList.remove('selected-checkout');
    }
    dayElem.classList.add('selected-checkout');
}

let selectedCheckinDate = null;
let selectedCheckoutDate = null;

// 달력 생성 및 초기화 함수
function initCalendar() {
    const today = new Date();
    const year = today.getFullYear();
    const month = today.getMonth() + 1;

    // 체크인 날짜 업데이트
    updateDate('checkin', formatDate(year, month, today.getDate()));

    // 체크아웃 날짜 선택 처리 (예시로 체크인 날짜보다 3일 뒤로 설정)
    const checkoutDate = new Date();
    checkoutDate.setDate(checkoutDate.getDate() + 3);
    updateDate('checkout', formatDate(checkoutDate.getFullYear(), checkoutDate.getMonth() + 1, checkoutDate.getDate()));

    // 모달에 선택된 날짜 표시
    updateDate('selectedCheckinDate', formatDate(year, month, today.getDate()));
    updateDate('selectedCheckoutDate', formatDate(checkoutDate.getFullYear(), checkoutDate.getMonth() + 1, checkoutDate.getDate()));

    createCalendar('calendarContainer', year, month, today.getDate());
}

// 월 표시 함수
function displayMonth(year, month) {
    const monthDisplay = document.getElementById('monthDisplay');
    monthDisplay.textContent = `${year}년 ${month}월`;
}

// 달력 내용 생성 함수
function createCalendar(containerId, year, month, selectedDay) {
    const container = document.getElementById(containerId);
    container.innerHTML = ''; // 기존 내용 삭제

    // 달력 컨테이너 생성
    // const calendarContainer = document.createElement('div');
    // calendarContainer.classList.add('calendar-container');
    // container.appendChild(calendarContainer);

    // 현재 월 달력
    createSingleCalendar(container, 'current-month', year, month, selectedDay);
    
    // 다음 월 달력
    const nextMonthYear = (month === 12) ? year + 1 : year;
    const nextMonthMonth = (month === 12) ? 1 : month + 1;
    createSingleCalendar(container, 'next-month', nextMonthYear, nextMonthMonth, null);

    
}


// 단일 달력 생성 함수
function createSingleCalendar(container, containerClass, year, month, selectedDay) {
    // ... (기존 달력 생성 코드는 그대로 유지) ...
    const singleContainer = document.createElement('div');
    singleContainer.classList.add('single-calendar');
    singleContainer.classList.add(containerClass);


    const daysInMonth = new Date(year, month, 0).getDate();
    const firstDay = new Date(year, month - 1, 1).getDay();
    // const today = new Date();    
    //월 생성
    displayMonth(year, month);
    // 달력 헤더
    const header = document.createElement('div');
    header.classList.add('calendar');
    const daysOfWeek = ['일', '월', '화', '수', '목', '금', '토'];
    for (const dayOfWeek of daysOfWeek) {
        const dayElem = document.createElement('div');
        dayElem.classList.add('day');
        dayElem.textContent = dayOfWeek;
        header.appendChild(dayElem);
    }
    singleContainer.appendChild(header);

    // 달력 내용
    const calendar = document.createElement('div');
    calendar.classList.add('calendar');
    for (let i = 0; i < firstDay; i++) {
        const dayElem = document.createElement('div');
        dayElem.classList.add('day');
        calendar.appendChild(dayElem);
    }
    for (let i = 1; i <= daysInMonth; i++) {
        const dayElem = document.createElement('div');
        dayElem.classList.add('day');
        dayElem.textContent = i;
        if (i === selectedDay) {
            dayElem.classList.add('selected-checkin');
        }
        
        dayElem.addEventListener('click', function (e) {
            // console.log(selectedCheckinDate)
            if (!selectedCheckinDate) {
                updateCheckinDate(year, month, i); // 체크인 날짜 업데이트
                updateDate('selectedCheckinDate', formatDate(year, month, i)); // 모달 내에 선택된 체크인 날짜 표시
                selectCheckin(dayElem); // 선택된 날짜에 클래스 부여                                
            }
            else if (!selectedCheckoutDate) {

                updateCheckoutDate(year, month, i); // 체크아웃 날짜 업데이트
                updateDate('selectedCheckoutDate', formatDate(year, month, i)); // 모달 내에 선택된 체크아웃 날짜 표시
                selectCheckout(dayElem); // 선택된 날짜에 클래스 부여 
                closeModal('checkinModal');
            }
            else if (selectedCheckoutDate) {
                updateCheckinDate(year, month, i); // 체크인 날짜 업데이트
                if (selectedCheckinDate < selectedCheckoutDate) {
                    console.log(e)
                    updateDate('selectedCheckinDate', formatDate(year, month, i)); // 모달 내에 선택된 체크인 날짜 표시
                    selectCheckin(dayElem); // 선택된 날짜에 클래스 부여  
                }
                else {
                    const selected = document.querySelectorAll('.selected-checkout');
                    for (const selectedDay of selected) {
                        selectedDay.classList.remove('selected-checkout');
                    }
                    updateDate('selectedCheckinDate', formatDate(year, month, i)); // 모달 내에 선택된 체크인 날짜 표시
                    selectCheckin(dayElem); // 선택된 날짜에 클래스 부여  
                    selectedCheckoutDate = null;
                }
            }



        });

        calendar.appendChild(dayElem);
    }
    container.appendChild(calendar);
}






// 오늘 날짜 포맷 함수
function formatDate(year, month, day) {
    return `${year}-${String(month).padStart(2, '0')}-${String(day).padStart(2, '0')}`;
}

// 체크인 날짜 업데이트
function updateCheckinDate(year, month, day) {
    const checkinDate = document.getElementById('checkin');
    checkinDate.textContent = formatDate(year, month, day);
    selectedCheckinDate = new Date(year, month - 1, day); // 선택된 체크인 날짜 저장
}
// 체크아웃 날짜 업데이트
function updateCheckoutDate(year, month, day) {
    const checkoutDate = document.getElementById('checkout');
    checkoutDate.textContent = formatDate(year, month, day);
    selectedCheckoutDate = new Date(year, month - 1, day); // 선택된 체크아웃 날짜 저장
}

// 페이지 로드 시 달력 초기화
window.addEventListener('DOMContentLoaded', function () {
    initCalendar();
});