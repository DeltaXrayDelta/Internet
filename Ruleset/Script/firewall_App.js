const data = $intent.parameter;
const write = $persistentStore.write(data, "targetApp");
$targetApp