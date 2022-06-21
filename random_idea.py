class idea():
    color =  82
    def __init__(self, title, desc, id, likes, tags=None):
        self.title = title
        self.desc = desc
        self.id = id
        self.likes = likes
        self.tags = []
        if tags:
            for i in tags:
                if i["value"][0] == "#":
                    self.tags.append(i["value"])
                else:
                    self.tags.append("#" + i["value"])
    
    
    
#   A super user friendly coordinate converter
#   ───────────────────────────────────────────
#   If you're a geocacher you know that you can
#   get coordinates that looks very different 
#   because they are using very different 
#   coordinate systems. Managing the transition
#   from a geocaching app to Google Maps for
#   instance is a pain because most systems that
#   help you with that aren't exactly helpful if
#   you're note already very into the world of
#   coordinate systems. Make a tool so that
#   anyone can do the task with ease. 
#   ──────────────────────────────────────────
#             ID: 2118    Likes: 13
#   ────────────────────────────────────────── 
#   #geograpichal #coordinates #conversion
#   #geocaching
    

    def represent(self) -> str:
        line_len = 40
        tab = 4

        description = ""
        space = 0
        if self.desc:
            description = list(self.desc)
            for i in range(len(description)):
                if description[i] == " ":
                    space = i
                if (i+1) % line_len == 0:
                    description[space] =  "\n    "
        
            description = "    " + "".join(description)
            
            description += "\n" + " "*tab + "─"*line_len + "\n"
        
        title = " "*tab + self.title + "\n" + " "*tab + "─"*line_len + "\n"

        metadat_len = 15 + len(str(self.id)) + len(str(self.likes))
        padding = line_len//2-metadat_len//2
        metadat = " "*tab + " "*padding + "ID: " + str(self.id) + "    " + "Likes: " + str(self.likes) + "\n"

        tags = ""
        if self.tags:
            tags = self.tags
            for i in range(len(tags)):
                if tags[i] == " ":
                    space = i
                if (i+1) % line_len == 0:
                    tags[space] =  " "*tab + "\n    "
        
            tags =  " "*tab +"─"*line_len + "\n" + "    " + " ".join(tags)

        whole = title + description + metadat + tags
        return whole

def main():
    import os
    import urllib.request
    import json
    import re
    
    os.system('color')

    URL = 'https://what-to-code.com/api/ideas/random'

    page = urllib.request.urlopen(URL)

    data = json.loads(page.read().decode("UTF-8"))
    idea_instance = idea(data["title"], re.sub("[\n ]+", " ", data["description"]), data["id"], data["likes"], data["tags"])
    
    print(f"\033[38;5;{idea.color}m" + idea.represent(idea_instance) + "\033[38;5;231m")
    
    return 0

if __name__ == "__main__":
    main()