INDEX_HTML := index.html
INDEX_CSS := $(wildcard *.css)
INDEX_JS = $(wildcard *.js)
INDEX_IMG = $(wildcard *.jpg)
WWWDIR := www

INDEX_FILES := $(INDEX_HTML) $(INDEX_CSS) $(INDEX_JS) $(INDEX_IMG)

SITE_FILES := $(patsubst %,$(WWWDIR)/%,$(INDEX_FILES))
SITE_INDEX_HTML := $(WWWDIR)/$(INDEX_HTML)

all: $(SITE_FILES)

$(WWWDIR):
	mkdir -p "$@"

$(SITE_INDEX_HTML): $(INDEX_HTML).py $(WWWDIR)
	./"$<" > "$@"

$(WWWDIR)/%.css: %.css $(WWWDIR)
	cp -a "$<" "$@"

$(WWWDIR)/%.js: %.js $(WWWDIR)
	cp -a "$<" "$@"

$(WWWDIR)/%.jpg: %.jpg $(WWWDIR)
	cp -a "$<" "$@"

.PHONY: test
test:
	$(SHELL) -c "cd "$(WWWDIR)" && python -m SimpleHTTPServer 8000 ."

clean:
	rm -rf "$(WWWDIR)"

print-%: ; @echo $*=$($*)

