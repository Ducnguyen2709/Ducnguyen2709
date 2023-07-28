let qno = 0;	//質問番号
let score = 0;	//得点

$('button').on('click', function(){

	// 次のターゲットの取得
	let next = $(this).data('next');

	if(  $(this).data('score') != undefined){
		score += Number( $(this).data('score') );
	}
	
	if( next == "#start"){

		// リセット
		score = 0;
		qno = 0;

	}else if( next == "#result" ){

		let msg;

		if( score >= 20){

			msg = "あなたは、Aです。";
		
		}else if( score <= 19 && score >= 1 ){
		
			msg = "あなたは、Bです。";
		
		}else{
		
			msg = "あなたは、Cです。";
		
		}

		$('.result__msg p').text(msg);
		
		splitText( $('.result__msg p') );
	
	}else{

		qno += 1;

		$(next).find('.quiz__no').text('Q-' + qno);
	}

	// 現状のターゲットからクラス削除
	$(this).closest('.stage').removeClass('active');

	setTimeout(function(){
		$(next).addClass('active');
	}, 100);
	
});

//テキスト分離
$('.scText').each( function() {
	
	splitText(this);

});

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