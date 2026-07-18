async function fetchData(name){
    const resp = await fetch(`https://embeflare.pythonanywhere.com/greet?name=${name}`);
    const data = await resp.json();
    if (!resp.ok){
        return 0;
    }
    return data;
}


async function run(){
    c = await fetchData("Alice");
    console.log(c);

}
run();