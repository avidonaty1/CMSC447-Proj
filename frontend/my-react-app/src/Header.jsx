import umbcLogo from "./assets/UMBC-primary-logo-RGB.png"


function Header(){
    return(
        <header>
            <img className="umbc-logo-img" src={umbcLogo} alt="UMBC Logo" />
            <h1 className="webpage-title">Custom 4 Year Plan Maker</h1>
        </header>
    )
}

export default Header