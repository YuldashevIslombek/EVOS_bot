let tg = window.Telegram.WebApp;
tg.expand();
tg.MainButton.textColor = "#FFFFFF";
tg.MainButton.color = "#af0808";

 // 1- Mahsulot
let count_1 = 0;
let count1 = document.getElementById("count1");
let addbtn1 = document.getElementById("addbtn1");
let rbtn1 = document.getElementById("rbtn1");

addbtn1.addEventListener("click", function (){
	count1.innerText = count_1 += 1;
	tg.MainButton.setText("To'lov");
	tg.MainButton.show();
});
rbtn1.addEventListener("click", function (){
	if (count_1 > 0) {
		count1.innerText = count_1 -= 1;
	}
	if (count_1 === 0){
		tg.MainButton.hide();
	}

});

// 2-Mahsulot
let count_2 = 0;
let count2 = document.getElementById("count2");
let addbtn2 = document.getElementById("addbtn2");
let rbtn2 = document.getElementById("rbtn2");

addbtn2.addEventListener("click", function (){
	count2.innerText = count_2 += 1;
	tg.MainButton.setText("To'lov");
	tg.MainButton.show();
});
rbtn2.addEventListener("click", function (){
	if (count_2 > 0) {
		count2.innerText = count_2 -= 1;
	}
	if (count_2 === 0){
		tg.MainButton.hide();
	}

});

// 3-Mahsulot
let count_3 = 0;
let count3 = document.getElementById("count3");
let addbtn3 = document.getElementById("addbtn3");
let rbtn3 = document.getElementById("rbtn3");

addbtn3.addEventListener("click", function (){
	count3.innerText = count_3 += 1;
	tg.MainButton.setText("To'lov");
	tg.MainButton.show();
});
rbtn3.addEventListener("click", function (){
	if (count_3 > 0) {
		count3.innerText = count_3 -= 1;
	}
	if (count_3 === 0){
		tg.MainButton.hide();
	}

});

// 4-Mahsulot
let count_4 = 0;
let count4 = document.getElementById("count4");
let addbtn4 = document.getElementById("addbtn4");
let rbtn4 = document.getElementById("rbtn4");

addbtn4.addEventListener("click", function (){
	count4.innerText = count_4 += 1;
	tg.MainButton.setText("To'lov");
	tg.MainButton.show();
});
rbtn4.addEventListener("click", function (){
	if (count_4 > 0) {
		count4.innerText = count_4 -= 1;
	}
	if (count_4 === 0){
		tg.MainButton.hide();
	}

});

// 5-Mahsulot
let count_5 = 0;
let count5 = document.getElementById("count5");
let addbtn5 = document.getElementById("addbtn5");
let rbtn5 = document.getElementById("rbtn5");

addbtn5.addEventListener("click", function (){
	count5.innerText = count_5 += 1;
	tg.MainButton.setText("To'lov");
	tg.MainButton.show();
});
rbtn5.addEventListener("click", function (){
	if (count_5 > 0) {
		count5.innerText = count_5 -= 1;
	}
	if (count_5 === 0){
		tg.MainButton.hide();
	}

});

// 6-Mahsulot
let count_6 = 0;
let count6 = document.getElementById("count6");
let addbtn6 = document.getElementById("addbtn6");
let rbtn6 = document.getElementById("rbtn6");

addbtn6.addEventListener("click", function (){
	count6.innerText = count_6 += 1;
	tg.MainButton.setText("To'lov");
	tg.MainButton.show();
});
rbtn6.addEventListener("click", function (){
	if (count_6 > 0) {
		count6.innerText = count_6 -= 1;
	}
	if (count_6 === 0){
		tg.MainButton.hide();
	}

});

// // 7-Mahsulot
// let count_7 = 0;
// let count7 = document.getElementById("count7");
// let addbtn7 = document.getElementById("addbtn7");
// let rbtn7 = document.getElementById("rbtn7");
//
// addbtn7.addEventListener("click", function (){
// 	count7.innerText = count_7 += 1;
// 	tg.MainButton.setText("To'lov");
// 	tg.MainButton.show();
// });
// rbtn7.addEventListener("click", function (){
// 	if (count_7 > 0) {
// 		count7.innerText = count_7 -= 1;
// 	}
// 	if (count_7 === 0){
// 		tg.MainButton.hide();
// 	}
//
// });
//
// // 8-Mahsulot
// let count_8 = 0;
// let count8 = document.getElementById("count8");
// let addbtn8 = document.getElementById("addbtn8");
// let rbtn8 = document.getElementById("rbtn8");
//
// addbtn8.addEventListener("click", function (){
// 	count8.innerText = count_8 += 1;
// 	tg.MainButton.setText("To'lov");
// 	tg.MainButton.show();
// });
// rbtn8.addEventListener("click", function (){
// 	if (count_8 > 0) {
// 		count8.innerText = count_8 -= 1;
// 	}
// 	if (count_8 === 0){
// 		tg.MainButton.hide();
// 	}
//
// });
//
