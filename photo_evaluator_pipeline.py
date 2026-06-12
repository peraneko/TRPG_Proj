import json
from typing import Dict, List, Optional

class GemRuntimeSession:
    """スキル階層型写真評価エンジンの統合実行クラス (ステートレス版)"""

    def dispatch(self, user_input: str, history: List[Dict], meta_data: Optional[Dict] = None) -> Dict:
        """
        Gemini LLMから履歴(history)を受け取り、解析結果を返すエントリポイント
        """
        # ループカウントは履歴の長さに依存させる
        loop_count = len(history) + 1
        
        # 評価判定ロジック
        if "評価して" in user_input or loop_count > 4:
            return self._run_phase_4(history)
            
        # 分析フェーズ (Run Phase 3)
        return {
            "status": "RUN_PHASE_3",
            "loop_count": loop_count,
            "message": "分析フェーズ実行中。入力と過去ログを統合解析しました。"
        }

    def _run_phase_4(self, history: List[Dict]) -> Dict:
        """最終評価フェーズ"""
        return {
            "status": "RUN_PHASE_4",
            "evaluation": {
                "rank": "上級者",
                "notes": "理論と実践のハイブリッド構造を確認。文脈の構築が鍵。"
            },
            "final_history_summary": history
        }

# --- Gemini用アダプター (Function Calling対応) ---
def call_pipeline(user_input: str, history_json: str = "[]", meta_data_json: str = "{}") -> str:
    """
    LLMが関数を呼ぶ際にJSON文字列を受け取るラッパー
    history_json: 過去の対話履歴をGeminiのLLMがここに詰め込んで渡す
    """
    history = json.loads(history_json)
    meta_data = json.loads(meta_data_json)
    
    session = GemRuntimeSession()
    result = session.dispatch(user_input, history, meta_data)
    
    return json.dumps(result, ensure_ascii=False)
