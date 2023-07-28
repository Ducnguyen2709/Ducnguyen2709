function splitText( target ){
	let html = '';
	let no = 0;
	// 取得した要素の中身、それぞれに対して処理できる
	$(target).contents().each( function(index) {
		//nodeType == 3 テキストノードの場合
		if (this.nodeType == 3) {
			let text = $(this).text();  //テキストの取得
			text.split('').forEach(function (letter, i) {
				no ++;
				if( letter !== ' ' ) {
					html += '<span style="transition-delay:'+((no - 1) * 50)+'ms">' + letter + '</span>';
				}else{
					html += letter;
				}
			});
		}else{
			html += this.outerHTML;
		}
	});
	$(target).html(html);
}