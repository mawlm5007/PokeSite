import React, { Component } from "react";

class Header extends Component {
    render() {
        return (
            <div className="text-center">
                <img
                    src="https://i.pinimg.com/originals/92/b5/c6/92b5c66a739ff9c405fe86ca062e1fe9.png"
                    width="100"
                    className="img-thumbnail"
                    style={{marginTop: "20px"}}
                />
                <h1> PokeSite </h1>
                <hr />
            </div>
        );
    }
}

export default Header;