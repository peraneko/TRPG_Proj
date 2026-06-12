# photo_evaluator_pipeline.py

class GemRuntimeSession:
    """スキル階層型写真評価エンジンの統合実行クラス（掛け合い強制・再デバッグ版）"""
    
    def __init__(self):
        self.loop_count = 0
        self.personas = ["批評家", "アウトプットちゃん", "フェチおねえさん", "アシスタント"]

    def dispatch(self, user_input):
        """システムのエントリーポイント：議論か評価かを判定"""
        self.loop_count += 1
        
        # 「評価して」のコマンド、または5ループ以上で評価フェーズへ
        if "評価して" in user_input or self.loop_count > 4:
            return self.run_phase_4()
            
        # それ以外は常に議論フェーズ（Phase 3）を呼び出す
        return self.run_phase_3(user_input)

    def run_phase_3(self, user_input):
        """ペルソナによる議論を強制発火させるためのプロンプト"""
        return (
            f"【議論モード起動】現在ループ回数: {self.loop_count}\n"
            "以下の4人のペルソナが、ユーザーの入力と提示された画像を基に、"
            "単なる同意は排除し、互いの意見を引用し矛盾を突き合うDiscord形式の掛け合いを行え。\n"
            "ペルソナ：批評家、アウトプットちゃん、フェチおねえさん、アシスタント\n"
            "議論の火種: ユーザーが提示した写真の「技術的意図」と「結果の乖離」。"
        )
    
    def run_phase_4(self):
        """評価モード：スキル階層判定フェーズ"""
        return "【評価モード起動】スキル階層プロトコル（初心者・中級者・上級者・プロ）に基づき、商業価値を判定せよ。"

    def get_evaluation_template(self):
        """評価用プロトコル定義"""
        return """
📸 写真分析・スキル階層プロトコル
Stage 1: 総合印象
Stage 2: 技術とスタイルの現状分析
Stage 3: 課題とソリューション
Stage 4: 成長と商用化ロードマップ
Stage 5: スキル階層判定 (初心者 / 中級者 / 上級者 / プロ)
"""

# エンジン起動
pipeline = GemRuntimeSession()


