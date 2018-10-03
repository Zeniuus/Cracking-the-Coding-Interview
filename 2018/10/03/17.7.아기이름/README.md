# 아기 이름
정부는 매년 가장 흔한 아기 이름 10,000개와 그 이름의 빈도수를 발표한다. 빈도수를 세는 데 아기 이름의 철자가 다르면 문제가 될 수 있다. 예를 들어 'John'과 'Jon'은 실제로는 같은 이르이지만 다르게 분류되는 것이다. 이름/빈도수 리스트와 같은 이름의 쌍이 리스트로 주어졌을 때 '실제' 빈도수의 리스트를 출력하는 알고리즘을 작성하라. 만약 John과 Jon이 동의어이고, Jon과 Johnny가 동의어라면 John과 Johnny도 동의어가 되어야 한다(이행성(transitive)와 대칭성(symmetric)을 만족한다). 최종 리스트에서는 동일하다면 아무 이름이나 사용해도 된다.

## Example
입력:
  * 이름: John (15), Jon (12), Chris (13), Kris (4), Christopher (19)
  * 동의어: (Jon, John), (John, Johnny), (Chris, Kris), (Chris, Christopher)
출력: John(27), Kris(36)
 