from app import app as dash_app
from app.layout import layout
import app.callbacks

dash_app.layout = layout

if __name__ == "__main__":
    dash_app.run(debug=True,host='0.0.0.0', port=8050)
