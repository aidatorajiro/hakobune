#include <stdio.h>
#include <SDL2/SDL.h>
#include <stdbool.h>

int WINDOW_WIDTH = 640;
int WINDOW_HEIGHT = 480;

double min = -5;
double max = 5;

SDL_Renderer* renderer;

SDL_Window *window;

double targetEquation(double x)
{
    return x*x*x;
}

int drawGraph()
{
    int points = WINDOW_WIDTH;

    double range = max - min;
    double unit = range / points;

    double x = min;
    double y = targetEquation(x);
    double prevX;
    double prevY;

    for (int i = 0; i < points; i++) {
        prevX = x;
        prevY = y;

        x += unit;
        y = targetEquation(x)/unit;

        SDL_RenderDrawLine(renderer, i, -prevY + WINDOW_HEIGHT/2, i + 1, -y + WINDOW_HEIGHT/2);
    }
}

int main(int argc, char* argv[])
{
    SDL_Init(SDL_INIT_VIDEO);

    window = SDL_CreateWindow(
        "An SDL Window",
        SDL_WINDOWPOS_UNDEFINED,
        SDL_WINDOWPOS_UNDEFINED,
        WINDOW_WIDTH,
        WINDOW_HEIGHT,
        SDL_WINDOW_OPENGL
      );

    renderer = SDL_CreateRenderer(window, -1, 0);

    if (window == NULL) {
        printf("Could not create window: %s\n", SDL_GetError());
        return 1;
    }

    SDL_Event ev;

    bool done = false;

    while (!done) {
        SDL_SetRenderDrawColor(renderer, 0, 0, 0, 255);
        SDL_RenderClear(renderer);
        SDL_SetRenderDrawColor(renderer, 255, 255, 255, SDL_ALPHA_OPAQUE);
        drawGraph();
        SDL_RenderPresent(renderer);
        while (SDL_PollEvent(&ev)) {
            if (ev.type == SDL_QUIT) {
                done = true;
            }
        }
    }

    SDL_DestroyRenderer(renderer);

    SDL_DestroyWindow(window);

    SDL_Quit();

    return 0;
}


