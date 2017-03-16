package jp.nobukatsu.TweetText;

import java.util.List;

/**
 * 文字列をつぶやき用に特定の文字数に分割するためのインタフェース
 * @author nobukatsu
 *
 */
public interface TweetTextIF {
    /**
     * 文字列をつぶやき用に特定の文字数に分割する。
     * @param text 分割したい文字列
     * @return 指定した文字数に分割された文字列が格納されたリスト。指定した文字数以下の場合はサイズが1のリストを返す。
     */
    public List<String> getTweetText(String text);
}