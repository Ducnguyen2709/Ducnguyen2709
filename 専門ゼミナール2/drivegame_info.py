# ゲーム内で扱う情報を辞書型で初期化
ginfo = {
    # 画面サイズ
    "rows": 20, # 画面のタイル行数
    "cols": 30, # 画面のタイル列数
    "tile_size": 32, # タイルのピクセルサイズ
    # 道路生成用
    "cx": 10, # 道路の左位置
    "size": 8, # 道路の広さ
    "dir": 0,  # 道路の向き
    "map_data": [], # 走行コースのマップデータ
    # プレイヤー管理用
    "car": 13, # 自動車のX座標
    "score": 0, # スコア
    # キャンバスや画像
    "cv": None, # 描画対象となるキャンバス
    "car_img": None # 自動車の画像
}
