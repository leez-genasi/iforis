function getPrevSession() {
    let files = app.vault.getMarkdownFiles()
        .filter(f => f.path.startsWith("a_sessions/"))
        .sort((a, b) => a.stat.ctime - b.stat.ctime);
    let prevSession = files[files.length - 2];

    return prevSession;
}

module.exports = getPrevSession;