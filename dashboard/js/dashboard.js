// ===============================
// WAF AI SOC v21.2 STABLE DASHBOARD
// ===============================

const attacks=document.getElementById("attacks");
const ips=document.getElementById("ips");
const score=document.getElementById("score");
const avgScore=document.getElementById("avgScore");

const topTable=document.getElementById("topTable");
const liveTable=document.getElementById("liveTable");
let lastAttackCount = 0;

const ctx=document.getElementById("chart").getContext("2d");

let chart=new Chart(ctx,{
    type:"line",
    data:{
        labels:[],
        datasets:[{
        label:"Attack Events",
        data:[],
        borderColor:"#00ff99",
        backgroundColor:"rgba(0,255,153,.15)",
        tension:.35,
        fill:true,
        pointRadius:4,
        pointHoverRadius:7,
        borderWidth:3
}]
    },
    options:{
        responsive:true,
        maintainAspectRatio:false,
        plugins:{
            legend:{
                labels:{
                    color:"#ffffff"
                }
            }
        },
        scales:{
            x:{
                ticks:{color:"#ffffff"},
                grid:{color:"#23354d"}
            },
            y:{
                beginAtZero:true,
                ticks:{color:"#ffffff"},
                grid:{color:"#23354d"}
            }
        }
    }
});

async function getStats(){

    const r = await fetch("/api/dashboard", {
        credentials: "include"
    });

    return await r.json();

}

async function getTop(){

    const r=await fetch("/api/top", {
    credentials:"include"
});
    return await r.json();

}

async function getLive(){

    const r=await fetch("/api/live", {
    credentials:"include"
});
    return await r.json();

}
async function refreshSystemHealth(){

    try{

        const r = await fetch("/api/system",{
            credentials:"include"
        });

        const data = await r.json();

        document.getElementById("defProcessor").textContent =
            data.services.processor === "active" ? "🟢 Active" : "🔴 Down";

        document.getElementById("sysApi").textContent =
            data.services.api === "active" ? "🟢 Active" : "🔴 Down";

        document.getElementById("sysCollector").textContent =
            data.services.collector === "active" ? "🟢 Active" : "🔴 Down";

        document.getElementById("sysProcessor").textContent =
            data.services.processor === "active" ? "🟢 Active" : "🔴 Down";

        document.getElementById("sysNginx").textContent =
            data.services.nginx === "active" ? "🟢 Active" : "🔴 Down";

        document.getElementById("sysFail2ban").textContent =
            data.services.fail2ban === "active" ? "🟢 Active" : "🔴 Down";

        document.getElementById("sysCpu").textContent =
            data.system.cpu.toFixed(1)+" %";

        document.getElementById("sysRam").textContent =
            data.system.ram.toFixed(1)+" %";

        document.getElementById("sysDisk").textContent =
            data.system.disk.toFixed(1)+" %";

        const h=Math.floor(data.system.uptime_seconds/3600);
        const m=Math.floor((data.system.uptime_seconds%3600)/60);

        document.getElementById("sysUptime").textContent=
            h+"h "+m+"m";

    }catch(err){

        console.error("System Health",err);

    }

}

function scoreClass(v){

    if(v>=75) return "critical";

    if(v>=50) return "high";

    if(v>=25) return "medium";

    return "low";

}

async function refreshDefenseStack(){

    try{

        const r = await fetch("/api/system",{
            credentials:"include"
        });

        const data = await r.json();

        document.getElementById("defFail2ban").textContent =
            data.services.fail2ban === "active" ? "🟢 Active" : "🔴 Down";

        document.getElementById("defModsec").textContent =
            data.defense.modsecurity === "active" ? "🟢 Active" : "🔴 Down";

        document.getElementById("defCRS").textContent =
            data.defense.crs === "active" ? "🟢 Active" : "🔴 Down";

        document.getElementById("defSQLite").textContent =
            data.defense.sqlite === "active" ? "🟢 Active" : "🔴 Down";

        document.getElementById("defUfw").textContent =
            data.defense.ufw === "active" ? "🟢 Active" : "🔴 Down";

    }catch(err){

        console.error("Defense Stack",err);

    }

}

async function refreshBlocked(){

    try{

        const r = await fetch("/api/blocked",{
            credentials:"include"
        });

        const data = await r.json();

        const box=document.getElementById("respLastIps");

        box.innerHTML="";

    data.blocked.forEach(item=>{

        box.innerHTML +=
       '<span class="blocked-ip">' +
       '🔴 ' +
       item.ip +
       ' <span class="blocked-score">' +
       '[' + item.score + ']' +
       '</span>' +
       '</span><br>';

});

    }catch(err){

        console.error("Blocked IPs",err);

    }

}


async function refreshDashboard(){

    const stats=await getStats();

    const top=await getTop();

    const live=await getLive();

    attacks.innerHTML=stats.total_attacks;

    ips.innerHTML=stats.unique_ips;

    score.innerHTML = stats.max_score || 0;

    avgScore.innerHTML = stats.avg_score || 0;

    let newAttacks = stats.total_attacks - lastAttackCount;

    lastAttackCount = stats.total_attacks;

    chart.data.labels.push(new Date().toLocaleTimeString());

    +chart.data.datasets[0].data.push(newAttacks);

    if(chart.data.labels.length>20){

        chart.data.labels.shift();

        chart.data.datasets[0].data.shift();

    }

    chart.update();

    topTable.innerHTML="";

    top.forEach(item=>{

        topTable.innerHTML+=`

        <tr>

            <td>${item[0]}</td>

            <td>${item[1]}</td>

        </tr>

        `;

    });

    liveTable.innerHTML="";

    live.forEach(item=>{

        liveTable.innerHTML+=`

        <tr>

            <td>${item[0]}</td>

            <td>${item[1]}</td>

            <td class="${scoreClass(item[2])}">

                ${item[2]}

            </td>

            <td>${item[3]}</td>

        </tr>

        `;

    });

}

refreshDashboard();
refreshSystemHealth();
refreshDefenseStack();
refreshBlocked();

setInterval(refreshDashboard,2000);
setInterval(refreshSystemHealth,5000);
setInterval(refreshDefenseStack,5000);
setInterval(refreshBlocked,5000);

// ===============================
// LAST UPDATE
// ===============================

const footer=document.querySelector("footer");

setInterval(()=>{

    footer.innerHTML=
    "WAF AI SOC v21.2 STABLE • Mohammed OUARDANI • 2026 • Last update:"
    + new Date().toLocaleString();

},1000);

// ===============================
// GLOBAL ERROR HANDLER
// ===============================

window.addEventListener("unhandledrejection",(e)=>{

    console.error(e.reason);

});

window.addEventListener("error",(e)=>{

    console.error(e.message);

});

