window.onload = function () {
	mmleditor.innerHTML += '<span id="editingnote"><span class="scale"></span><span class="fluctuations"></span><span class="length"></span></span><span id="nextnote"></span>';
	
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
		editingParent = nextnote.parentNode;
		
		if (e.keyCode == 8) {//削除ボタンが押されたら
			editingParent.removeChild(editingnote);
			editingParent.children[editingParent.children.length - 2].id = "editingnote";
		}
		
		if (textinput.value.match(/([cdefgabr])/)) {
			if (check()) {
				editingnote.id = "";
				nextnote.id = "editingnote";
				editingnote.innerHTML = '<span class="scale">' + RegExp.$1 + '</span><span class="fluctuations"></span><span class="length"></span>';
				editingnote.parentNode.innerHTML += '<span id="nextnote"></span>';
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