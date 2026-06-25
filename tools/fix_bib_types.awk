#!/usr/bin/awk -f
# Fix @article entries that carry a `booktitle` (and no `journal`):
# apacite ignores booktitle on @article, silently dropping the venue and (with a
# url and no doi) emitting "literal stack isn't empty" errors. Reclassify each by
# its venue string so the venue renders correctly.
BEGIN { RS = "@"; ORS = "" }
NR == 1 { print; next }   # leading text before first @ (usually empty)

{
    rec = $0
    is_article = (rec ~ /^article[ \t]*\{/)
    has_bt = (rec ~ /\n[ \t]*booktitle[ \t]*=/)
    has_journal = (rec ~ /\n[ \t]*journal[ \t]*=/)

    if (is_article && has_bt && !has_journal) {
        # extract booktitle value for classification
        bt = rec
        sub(/.*\n[ \t]*booktitle[ \t]*=[ \t]*\{/, "", bt)
        sub(/\}.*/, "", bt)

        if (bt ~ /Computing Surveys|Transactions|Computational Linguistics|TMLR|Machine Learning Research|TACL|(^|[^a-zA-Z])Science([^a-zA-Z]|$)|Nature|Lancet|PLoS|Big Data|Journal|JDIQ|IEEE Access|Frontiers of Computer Science|Annals|Newsletter|PNAS/) {
            # genuine journal: keep @article, booktitle -> journal
            sub(/\n([ \t]*)booktitle([ \t]*)=/, "\n  journal =", rec)
            print "@" rec
        } else if (bt ~ /MIT Press|NYU Press|University Press/) {
            # book: @article -> @book, booktitle -> publisher
            sub(/^article/, "book", rec)
            sub(/\n([ \t]*)booktitle([ \t]*)=/, "\n  publisher =", rec)
            print "@" rec
        } else if (bt ~ /ProPublica|SSRN|Working Paper/) {
            # report/preprint: @article -> @misc, booktitle -> howpublished
            sub(/^article/, "misc", rec)
            sub(/\n([ \t]*)booktitle([ \t]*)=/, "\n  howpublished =", rec)
            print "@" rec
        } else {
            # conference paper: @article -> @inproceedings (keeps booktitle)
            sub(/^article/, "inproceedings", rec)
            print "@" rec
        }
    } else {
        print "@" rec
    }
}
