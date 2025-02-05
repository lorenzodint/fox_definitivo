import streamlit as st


def html_component(tag, testo, css):
    
    html = f'''<{tag} class="'''
    
    classi = ""
    for classe in css:
        classi += classe + " "
    
    html += classi + '">'
    
    html += testo + f'''</{tag}>'''
    
    return html
    



# if __name__ == "__main__":
    
#     print(html_component(css=["prima","seconda", "terza"]))

