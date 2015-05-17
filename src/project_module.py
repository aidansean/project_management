class project_object:
    def __init__(self,name,title):
        self.name   = name
        self.title  = title
        self.domain = ''
        self.links  = []
        self.preview_image_uri = ''
        self.github_repo_name = ''
        self.introduction = ''
        self.overview = ''
        self.challenges = []
        self.status = 'idea'
        self.mathjax = False
    
    def github_uri(self):
        return 'https://github.com/aidansean/%s'%self.github_repo_name
    def wordpress_text(self):
        lines = []
        if self.mathjax:
            lines.append('[mathjax]')
        lines.append(self.introduction)
        
        link_lines = []
        for l in self.links:
            link_lines.append(l.html())
        if not self.github_repo_name=='':
            link_lines.append('<a href="%s">GitHub repository</a>'%self.github_uri())
        if len(link_lines)>0:
            lines.append('<h3>Links</h3>')
            lines.append('\n'.join(link_lines))
        
        if not self.overview=='':
            lines.append('<h3>Overview</h3>')
            lines.append(self.overview)
            
        
        challenge_lines = []
        challenge_lines.append('<h3>Challenges</h3>')
        challenge_lines.append('<dl>')
        for c in self.challenges:
            challenge_lines.append(c.html())
        challenge_lines.append('</dl>')
        if len(self.challenges)>0:
            lines.append('\n'.join(challenge_lines))
        
        return '\n\n'.join(lines)
    def PHP_text(self):
        lines = []
        lines.append('<?php')
        lines.append('$github_uri   = "%s" ;'%self.github_uri())
        lines.append('$blogpost_uri = "http://aidansean.com/projects/?tag=%s" ;'%self.name)
        lines.append('?>')
        
        return '\n'.join(lines)
            

class image_object:
    def __init__(self, uri, w, h):
        self.uri = uri
        self.w   =   w
        self.h   =   h

class challenge_object:
    def __init__(self, challenge_text, solution_text, status):
        self.challenge_text = challenge_text
        self.solution_text  = solution_text
        self.status         = status
    def html(self):
        text = []
        text.append('<dt><em>Challenge</em>: %s</dt>'%self.challenge_text)
        text.append('<dd><em>Solution</em>: %s (%s)</dd>'%(self.solution_text, self.status))
        return '\n\n'.join(text)

class link_object:
    def __init__(self,domain,path,text):
        self.domain = domain
        self.path = path
        self.text = text
    def html(self):
        return '<a href="%s%s">%s</a>'%(self.domain, self.path, self.text) ;


