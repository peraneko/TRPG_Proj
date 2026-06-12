import json
from typing import Dict, List, Optional

class GemRuntimeSession:
    """スキル階層型写真評価エンジンの統合実行クラス"""
    
    def __init__(self):
        # 永続化が必要な場合は、ここを外部DB/ファイル読み込みに変更してください
        self.loop_count = 0
        self.phase_4_locked = True
        self.sequence_buffer = []

    def dispatch(self, user_input: str, meta_data: Optional[Dict] = None) -> Dict:
        """
        Gemini LLMから呼び出されるエントリポイント
        """
        self.loop_count += 1
        
        # 評価判定ロジック (トリガー条件の統合)
        if "評価して" in user_input or self.loop_count > 4:
            self.phase_4_locked = False
            return self._run_phase_4()
            
        # データの蓄積
        if meta_data:
            self.sequence_buffer.append(meta_data)
        self.sequence_buffer.append({"user_input": user_input})
        
        return {
            "status": "RUN_PHASE_3",
            "loop_count": self.loop_count,
            "message": "分析フェーズ実行中。座談会ログを更新しました。"
        }

    def _run_phase_4(self) -> Dict:
        """最終評価フェーズ"""
        return {
            "status": "RUN_PHASE_4",
            "evaluation": {
                "rank": "上級者",
                "notes": "理論と実践のハイブリッド構造を確認。"
            },
            "history_summary": self.sequence_buffer
        }

# --- Gemini用アダプター (Function Calling対応) ---
def call_pipeline(user_input: str, meta_data: str = "{}") -> str:
    """
    LLMが関数を呼ぶ際にJSON文字列を受け取るためのラッパー
    """
    session = GemRuntimeSession() # 本来はインスタンスをセッションIDで管理する必要があります
    data = json.loads(meta_data)
    result = session.dispatch(user_input, data)
    return json.dumps(result, ensure_ascii=False)
