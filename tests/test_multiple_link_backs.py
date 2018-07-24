import re

from sphinx_testing import with_app


@with_app(buildername='html', srcdir='doc_test/multiple_link_backs')
def test_multiple_link_backs(app, status, warning):
    app.builder.build_all()
    html = (app.outdir / 'index.html').read_text()

    links_to = re.findall("#R_12346", html)
    assert len(links_to) == 2