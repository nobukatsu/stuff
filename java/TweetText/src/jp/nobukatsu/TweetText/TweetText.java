package jp.nobukatsu.TweetText;

import java.util.List;
import java.util.ArrayList;

/**
 * TweetTextIFを実装したクラス。
 * @author nobukatsu
 *
 */
public class TweetText implements TweetTextIF{
    
    private int tweetLength = 140; // 最大つぶやき文字数
    private String suffix = "(続く)"; // 140文字を超えた場合の接尾語
    private String prefix = "(続き)"; // 140文字を超えた場合の2番目以降の接頭語

    @Override
    public List<String> getTweetText(String text) {
	
	List<String> tweetText = new ArrayList<String>();
	
	// 文字列が最大つぶやき文字数以下の場合
	if(text.length() <= tweetLength){
	    tweetText.add(text);
	    return tweetText;

	// 文字列が最大つぶやき文字数より大きい場合
	}else{ 
	    // 最大つぶやき文字数以下になるまで続ける
	    while(text.length() >= tweetLength){
		tweetText.add(text.substring(0, tweetLength-suffix.length()) + suffix); // 接尾語をつけてリストに追加
		text = prefix + text.substring(tweetLength-suffix.length()); // 残りを接頭語をつけて変数に格納
	    }
	    tweetText.add(text); // 140文字以下になった最後の文字列をリストに追加
	    return tweetText;
	}
    }
}
