# 21 Blackjack Game
Welcome to the Customized Blackjack Game, a Python project created by Amaury Junior to practice programming skills. This game is inspired by Blackjack but includes some unique rules to make it a distinct gaming experience.

## Game Description

The Customized Blackjack Game is a command-line application that puts a spin on the traditional Blackjack game. It features modified rules for an engaging and challenging gameplay.

![Inittial Screen](docs/inittial_screen.png)

[**Live Website: 21 Blackjack Game**](https://gameblackjack-a1c3e6bb9955.herokuapp.com/)

## User Experience (UX)

### New User

1. As a first-time user, I want to be able to start a game without having to read extensive rules.

2. If I encounter any issues or want to provide feedback, I'd like a way to contact the developer.

3. Most importantly, I want to have a fun and engaging experience!

### Returning User

1. As a returning user, I want to quickly start playing the game again.

2. I'd like to easily check if there have been any updates or changes to the game.

3. I'm here to have fun once more!

### Frequent User Goals

1. As a frequent user, my main goal is to continue enjoying the game.

2. I'll occasionally check for any updates or new features to enhance my experience.

3. The most important thing for me is to have an entertaining time playing!

## Game Flow

![FlowChart](docs/flow_chart.png)

The game starts with the player receiving two cards. The objective is to reach 21 points or as close as possible without exceeding. If the player has less than 15 points, they are automatically required to draw more cards until they reach 15 points or more. Once 15 points or more are achieved, the player can choose to 'STAND' to keep their current score or 'HIT' to receive an additional card. Once the player finishes their turn, it's the dealer's turn. The dealer always 'HITs' until they reach 17 points or more. If the player or dealer exceeds 21 points, it is considered a 'BUST'. The winner of the round is determined based on who is closest to 21 points. The game consists of five rounds, and the player with the most wins at the end is declared the winner.

## Design Choices

The project aimed to create a terminal-based application with interactive and seamless transitions to provide an intuitive User Experience (UX). Visual elements were strategically incorporated to enhance user interaction and improve the game's visual appeal, as demonstrated in the Features section.

## Features

As part of the game, the 'Welcome Screen' serves as the initial interface where players are greeted and introduced to the game. It features the game's logo, providing options for players to navigate through the menu.

![Welcome Screen](docs/inittial_screen.png)