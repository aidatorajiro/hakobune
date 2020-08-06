window.onload = function () {
	mmleditor.innerHTML += '<span id="editingnote"><span class="scale"></span><span class="fluctuations"></span><span class="length"></span></span>';
	
	function check() {
		if (length.className == "length no") {
			length.innerHTML = "";
			textinput.value = "";
			return false;
		}
		
		return true;
	}
	
	textinput.onkeyup = function (e) {
		scale = editingnote.getElementsByClassName("scale")[0];
		length = editingnote.getElementsByClassName("length")[0];
		fluctuations = editingnote.getElementsByClassName("fluctuations")[0];
		editingParent = editingnote.parentNode;
		
		if (e.keyCode == 8) {//削除ボタンが押されたら
			editingnote.previousSibling.id = "next_editingnote";
			editingParent.removeChild(editingnote);
			next_editingnote.id = "editingnote";
		}
		
		if (textinput.value.match(/([cdefgabr])/)) {
			if (check()) {
				editingnote.id = "prev_editingnote";
				var newnote = document.createElement('span');
				newnote.id = "editingnote";
				newnote.innerHTML = '<span class="scale">' + RegExp.$1 + '</span><span class="fluctuations"></span><span class="length"></span>';
				editingParent.insertBefore(newnote, prev_editingnote.nextSibling);
				prev_editingnote.id = "";
			}
		}
		
		if (textinput.value.match(/(\d)/)) {
			length.innerHTML += RegExp.$1;
			
			length.className = "length no";
			if ((length.innerHTML & (length.innerHTML - 1)) == 0) {//2の冪乗かチェック
				length.className = "length ok";
			}
		}
		
		if (textinput.value.match(/([+-])/)) {
			fluctuations.innerHTML += RegExp.$1;
		}
		
		textinput.value = "";
	};
};