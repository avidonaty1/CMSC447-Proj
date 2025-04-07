import umbcLogo from "./assets/UMBC-primary-logo-RGB.png"


function Header(){
    return(
        <header>
            <img class="umbc-logo-img" src={umbcLogo} alt="UMBC Logo" />
            <h1 class="webpage-title">4-Year Academic Pathway</h1>
        </header>
    )
}

export default Header