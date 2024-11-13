def write_file(filename, content):
	with open(filename, "w") as file:
		file.write(content)

# section holder
class Holder:
	def __init__(self, content):
		self.content = content
	def __str__(self):
		return self.content.__str__()
	def get(self):
		return self.content.get()
	def add_holder(self, holder):
		holder.content = self.content
		self.content = holder

class Section(Holder):
	def __init__(self, title, content):
		self.title = title
		self.content = content
	def __str__(self):
		return f"### {self.title if self.title != '' else ''}\n{self.content}\n"

class Align(Holder):
	def __init__(self, align, content):
		self.align = align
		self.content = content
	def __str__(self):
		return f'<div align="{self.align}">\n{self.content}\n</div>'

# section type
class Empty:
	def __str__(self):
		return ""
	def get(self):
		return self

class Images(Empty):
	def __init__(self, height=None):
		self.images = []
		self.height = height
	def add_image(self, url, alt):
		self.images.append((url, alt))
	def __str__(self):
		return "\n".join([f"<img src='{url}' alt='{alt}'{f' height={self.height}' if self.height else ''}>" for url, alt in self.images])

class Logos(Empty):
	def __init__(self):
		self.logos = []
	def add_logo(self,alt, url, link):
		self.logos.append((url, alt, link))
	def __str__(self):
		return "".join([f'<a href="{link}"><img src="{url}" alt="{alt}" height="30" width="30"></a>\n<img width="12"/>\n' for url, alt, link in self.logos])

class Texts(Empty):
	def __init__(self):
		self.texts = []
	def add_text(self, text):
		self.texts.append(text)
	def __str__(self):
		return "\\\n".join(self.texts)

class Table(Empty):
	def __init__(self):
		self.rows = []
	def add_row(self, cells):
		if len(self.rows) != 0 and len(cells) != len(self.rows[0]):
			raise ValueError(f"Row of a table must have the same length, row 0 has {len(self.rows[0])} columns, but row {len(self.rows)} has {len(cells)} columns\n{self.rows[0]}\n{cells}")
		self.rows.append(cells)
	def get_row(self, index):
		return self.rows[index]
	def __str__(self):
		table = "<table>\n"
		for row in self.rows:
			table += "<tr>\n"
			for cell in row:
				table += f"<td>{cell}</td>\n"
			table += "</tr>\n"
		table += "</table>"
		return table

if __name__ == "__main__":
	sections = {
		"about_me": Section("📖 About me", Texts()),
		"github_stats": Section("📈 Github Stats", Images(height=150)),
		"known_languages": Section("🚀 Known Languages", Logos()),
		"known_tools": Section("🛠️ Known Tools", Logos()),
		"languages_seen": Section("🔍 Languages Seen", Logos()),
		"tools_seen": Section("🔍 Tools Seen", Logos()),
		"tier_list": Section("🏆 Tier List", Logos()),
		"snake": Section("", Images())
	}

	# About me
	sections["about_me"].get().add_text("Hello I'm Rignchen, a swiss app dev student passionated in programmation.")
	sections["about_me"].get().add_text("I've been coding in mcfunction since I was 14 and learned python when I was 16.")
	sections["about_me"].get().add_text("I code for around 2-3 hours for fun and 7 hours for work, this number can go up to 12 hours during vacations.")
	sections["about_me"].get().add_text("I like strict and optimized languages, that's why my favorite language is rust.")
#	sections["about_me"].get().add_text("

	# Github Stats
	sections["github_stats"].add_holder(Align("center", Empty()))
	sections["github_stats"].get().add_image("https://github-readme-stats.vercel.app/api?username=Rignchen&show_icons=true&theme=dark#gh-dark-mode-only", "Stats Graph")
	sections["github_stats"].get().add_image("https://github-readme-stats.vercel.app/api/top-langs?username=Rignchen&locale=en&hide_title=false&layout=compact&card_width=320&langs_count=5&theme=dracula&hide_border=false", "Languages Graph")
#	sections["github_stats"].get().add_image("

	# Languages
	sections["known_languages"].add_holder(Align("left", Empty()))
	sections["known_languages"].get().add_logo("Python", "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg", "https://www.python.org/")
	sections["known_languages"].get().add_logo("Java", "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/java/java-original.svg", "https://www.java.com/")
	sections["known_languages"].get().add_logo("Rust", "https://www.rust-lang.org/static/images/rust-logo-blk.svg", "https://www.rust-lang.org/")
	sections["known_languages"].get().add_logo("SQLite", "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/sqlite/sqlite-original.svg", "https://www.sqlite.org/")
	sections["known_languages"].get().add_logo("PostgreSQL", "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/postgresql/postgresql-original.svg", "https://www.postgresql.org/")
	sections["known_languages"].get().add_logo("PHP", "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/php/php-original.svg", "https://www.php.net/")
#	sections["known_languages"].get().add_logo("

	# Tools
	sections["known_tools"].add_holder(Align("left", Empty()))
	sections["known_tools"].get().add_logo("VSCode", "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/vscode/vscode-original.svg", "https://code.visualstudio.com/")
	sections["known_tools"].get().add_logo("Git", "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/git/git-original.svg", "https://git-scm.com/")
	sections["known_tools"].get().add_logo("GitHub", "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/github/github-original.svg", "https://github.com")
	sections["known_tools"].get().add_logo("JetBrains", "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/jetbrains/jetbrains-original.svg", "https://www.jetbrains.com/")
	sections["known_tools"].get().add_logo("Docker", "https://cdn.worldvectorlogo.com/logos/docker.svg", "https://www.docker.com/")
	sections["known_tools"].get().add_logo("Vim", "https://upload.wikimedia.org/wikipedia/commons/9/9f/Vimlogo.svg", "https://www.vim.org/")
#	sections["known_tools"].get().add_logo("

	# Languages Seen
	sections["languages_seen"].add_holder(Align("left", Empty()))
	sections["languages_seen"].get().add_logo("C", "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/c/c-original.svg", "https://en.wikipedia.org/wiki/C_(programming_language)")
	sections["languages_seen"].get().add_logo("html", "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/html5/html5-original.svg", "https://developer.mozilla.org/docs/Web/HTML")
	sections["languages_seen"].get().add_logo("css", "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/css3/css3-original.svg", "https://developer.mozilla.org/docs/Web/CSS")
	sections["languages_seen"].get().add_logo("JavaScript", "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/javascript/javascript-original.svg", "https://developer.mozilla.org/docs/Web/JavaScript")
	sections["languages_seen"].get().add_logo("TypeScript", "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/typescript/typescript-original.svg", "https://www.typescriptlang.org/")
	sections["languages_seen"].get().add_logo("F#", "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/fsharp/fsharp-original.svg", "https://fsharp.org/")
	sections["languages_seen"].get().add_logo("D lang", "https://upload.wikimedia.org/wikipedia/commons/2/24/D_Programming_Language_logo.svg", "https://dlang.org/")
	sections["languages_seen"].get().add_logo("Objective-C", "https://seeklogo.com/images/O/objective-c-logo-81746870EF-seeklogo.com.png", "https://developer.apple.com/documentation/objectivec")
#	sections["languages_seen"].get().add_logo("

	# Tools Seen
	sections["tools_seen"].add_holder(Align("left", Empty()))
	sections["tools_seen"].get().add_logo("Angular", "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/angularjs/angularjs-original.svg", "https://angular.io/")
	sections["tools_seen"].get().add_logo("Figma", "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/figma/figma-original.svg", "https://www.figma.com/")
#	Sections["tools_seen"].get().add_logo("

	# Tier List

	# Snake
	sections["snake"].add_holder(Align("center", Empty()))
	sections["snake"].get().add_image("https://raw.githubusercontent.com/Rignchen/Rignchen/output/snake.svg", "Snake Animation")
#	sections["snake"].get().add_image("

	# Write the README
	write_file("README.md", f'''# Hi there <img src="https://media.giphy.com/media/hvRJCLFzcasrR4ia7z/giphy.gif" width="25px"> </h1>

{sections["about_me"]}
---
{sections["github_stats"]}
---
{sections["known_languages"]}
{sections["known_tools"]}
{sections["languages_seen"]}
{sections["tools_seen"]}
---
{sections["snake"]}''')

