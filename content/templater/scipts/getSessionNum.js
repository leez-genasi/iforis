function getSessionNum(tp) {
    let files = app.vault.getMarkdownFiles().filter(
        f => f.path.startsWith("sessions/"));
    let num = String(files.length);

    while (num.length < 3) {
        num = "0" + num;
    }
    
    return num;
}

module.exports = getSessionNum