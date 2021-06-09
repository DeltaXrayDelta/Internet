const read = $persistentStore.read("targetApp");
$done({ matched: Boolean(read) });