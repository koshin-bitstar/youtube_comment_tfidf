### How to setup
GCPからAPIキーとGOOGLE_APPLICATION_CREDENTIALSのJSONを取得してください。
そのあと、.example.env を参考に.envを設定してください。

#### VIDEO_ID
`https://www.youtube.com/watch?v=<ビデオID>`

### How to exec
#### 仮想環境を作って動かす
`python3 -m venv myenv` or `python -m venv myenv`<br />
`source myenv/bin/activate`<br />
`pip install -r requirements.txt`<br />
`python app.py`<br />
※ 最初の実行はちょっと時間がかかります。
