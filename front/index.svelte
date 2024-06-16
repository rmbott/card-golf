<script>let name = "";
function getName() {
    fetch("../name").then(d => d.text()).then(d => (name = d));
    }
</script>
<main>
    <h1>Hello {name}!</h1>
    <button on:click={getName}>Get name</button>
</main>