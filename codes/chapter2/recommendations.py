# coding: UTF-8

# 映画の評者といくつかの映画に対する彼らの評価ディクショナリ
critics={'Lisa Rose': {'Lady in the Water': 2.5, 'Snakes on a Plane': 3.5,
 'Just My Luck': 3.0, 'Superman Returns': 3.5, 'You, Me and Dupree': 2.5,
 'The Night Listener': 3.0},
'Gene Seymour': {'Lady in the Water': 3.0, 'Snakes on a Plane': 3.5,
 'Just My Luck': 1.5, 'Superman Returns': 5.0, 'The Night Listener': 3.0,
 'You, Me and Dupree': 3.5},
'Michael Phillips': {'Lady in the Water': 2.5, 'Snakes on a Plane': 3.0,
 'Superman Returns': 3.5, 'The Night Listener': 4.0},
'Claudia Puig': {'Snakes on a Plane': 3.5, 'Just My Luck': 3.0,
 'The Night Listener': 4.5, 'Superman Returns': 4.0,
 'You, Me and Dupree': 2.5},
'Mick LaSalle': {'Lady in the Water': 3.0, 'Snakes on a Plane': 4.0,
 'Just My Luck': 2.0, 'Superman Returns': 3.0, 'The Night Listener': 3.0,
 'You, Me and Dupree': 2.0},
'Jack Matthews': {'Lady in the Water': 3.0, 'Snakes on a Plane': 4.0,
 'The Night Listener': 3.0, 'Superman Returns': 5.0, 'You, Me and Dupree': 3.5},
'Toby': {'Snakes on a Plane':4.5,'You, Me and Dupree':1.0,'Superman Returns':4.0}}

from math import sqrt

# person1とperson2の距離を基にした類似性スコアを返す
def sim_distance(prefs,person1,person2):
  # 二人とも評価しているアイテムのリストを得る
  si={}
  for item in prefs[person1]:
    if item in prefs[person2]: si[item]=1

  # 共通して評価しているものが一つもなければ0を返す
  if len(si)==0: return 0

  # すべての差の平方を足し合わせる
  sum_of_squares=sum([pow(prefs[person1][item]-prefs[person2][item],2)
                      for item in prefs[person1] if item in prefs[person2]])

  return 1/(1+sqrt(sum_of_squares))

# p1とp2のピアソン相関係数を返す
def sim_pearson(prefs,p1,p2):
  # 両者がお互いに評価しているアイテムを取得
  si={}
  for item in prefs[p1]:
    if item in prefs[p2]: si[item]=1

  # 要素の数を調べる
  n=len(si)

  # 共通して評価しているものが一つもなければ0を返す
  if n==0: return 0

  # すべての嗜好を合計する
  sum1=sum([prefs[p1][it] for it in si])
  sum2=sum([prefs[p2][it] for it in si])

  # 平方を合計する
  sum1Sq=sum([pow(prefs[p1][it],2) for it in si])
  sum2Sq=sum([pow(prefs[p2][it],2) for it in si])

  # 積を合計する
  pSum=sum([prefs[p1][it]*prefs[p2][it] for it in si])

  # ピアソンによるスコアを計算する
  num=pSum-(sum1*sum2/n)
  den=sqrt((sum1Sq-pow(sum1,2)/n)*(sum2Sq-pow(sum2,2)/n))
  if den==0: return 0

  r=num/den

  return r

# ディクショナリprefsからpersonにもっともマッチするものたちを返す
# 結果の数と類似性関数はオプションのパラメーター
def topMatches(prefs,person,n=5,similarity=sim_pearson):
  scores=[(similarity(prefs,person,other),other)
                  for other in prefs if other!=person]
  # 高スコアがリストの最初に来るように並び替える
  scores.sort()
  scores.reverse()
  return scores[0:n]
