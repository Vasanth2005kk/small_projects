const MonthName = document.getElementsByClassName('month-name');
const DayName = document.getElementsByClassName('dayname');
const Day = document.getElementsByClassName('day');
const Year = document.getElementsByClassName('year');

const d = new Date();

Array.from(MonthName).forEach(element => {
  element.innerHTML = d.toLocaleString('en', { month: 'long' });
});


Array.from(DayName).forEach(element => {
  element.innerHTML = d.toLocaleString('en', { weekday: 'long' });
});

Array.from(Day).forEach(element => {
  element.innerHTML = d.getDate();
});


Array.from(Year).forEach(element => {
  element.innerHTML = d.getFullYear();
});
