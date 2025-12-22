function clearForms () {
    forms = document.getElementsByClassName('form')[0]
    forms.reset()
}

document.addEventListener("DOMContentLoaded", () => { 
    const times_to_format = document.getElementsByClassName("format-time")
    for (const el of times_to_format) {
        const segundos = parseInt(el.textContent.trim(), 10)

        if (isNaN(segundos)) continue

        const horas = Math.floor(segundos / 3600)
        const minutos = Math.floor((segundos % 3600) / 60)

        const horasFmt = horas.toString().padStart(2, "0")
        const minutosFmt = minutos.toString().padStart(2, "0")

        el.textContent = `${horasFmt}:${minutosFmt}`
    }
});

document.addEventListener("DOMContentLoaded", () => {

    const datetimes = document.getElementsByClassName("format-datetime")

    for (const el of datetimes) {
        const valor = el.textContent.trim()

        const [data, hora] = valor.split(" ")
        const [ano, mes, dia] = data.split("-")

        const novoFormato = `${dia}/${mes}/${ano} ${hora}`

        el.textContent = novoFormato
    }
})