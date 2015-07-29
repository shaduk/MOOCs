//
// breakout.c
//
// Computer Science 50
// Problem Set 3
//

// standard libraries
#define _XOPEN_SOURCE
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

// Stanford Portable Library
#include <spl/gevents.h>
#include <spl/gobjects.h>
#include <spl/gwindow.h>

// height and width of game's window in pixels
#define HEIGHT 600
#define WIDTH 400

// number of rows of bricks
#define ROWS 5

// number of columns of bricks
#define COLS 10

// radius of ball in pixels
#define RADIUS 10

// lives
#define LIVES 3

// prototypes
void initBricks(GWindow window);
GOval initBall(GWindow window);
GRect initPaddle(GWindow window);
GLabel initScoreboard(GWindow window);
void updateScoreboard(GWindow window, GLabel label, int points);
GObject detectCollision(GWindow window, GOval ball);
void removeGWindow(GWindow gw, GObject gobj);



int main(void)
{
    // seed pseudorandom number generator
    srand48(time(NULL));

    // instantiate window
    GWindow window = newGWindow(WIDTH, HEIGHT);

    // instantiate bricks
    initBricks(window);

    // instantiate ball, centered in middle of window
    GOval ball = initBall(window);

    // instantiate paddle, centered at bottom of window
    GRect paddle = initPaddle(window);

    // instantiate scoreboard, centered in middle of window, just above ball
    GLabel label = initScoreboard(window);

    // number of bricks initially
    int bricks = COLS * ROWS;

    // number of lives initially
    int lives = LIVES;

    // number of points initially
    int points = 0;
    double velocity = drand48()/20;
    double velocityx = velocity;
    double velocityy = velocity;
    // keep playing until game over
    
    while (lives > 0 && bricks > 0)
    {
        GEvent event = getNextEvent(MOUSE_EVENT);
       
        
        if(event != NULL)
        {
            if(getEventType(event) == MOUSE_MOVED)
            {
                double x = getX(event) - getWidth(paddle)/2;
                if(x >= 0 && x <= 400-getWidth(paddle))
                {
                    setLocation(paddle, x, 550);
                
                }
                else if(x < 0)
                {
                    setLocation(paddle,0,550);
                }
                else if(x >= 400-getWidth(paddle))
                {
                    setLocation(paddle,400-getWidth(paddle),550);
                }
                
            }
        }
        
        move(ball, velocityx,velocityy);
        // Right collision
        if(getX(ball) + getWidth(ball) >= getWidth(window))
        {
            velocityx = -velocityx;
           
        }
        //Left Collision
        else if(getX(ball) <= 0)
        {
            velocityx = -velocityx;
            
        }
        
        if(getY(ball) + getHeight(ball) >= getHeight(window))
        {
            lives = lives - 1;
            GEvent event1 = getNextEvent(MOUSE_EVENT);
            if(event1!=0)
            {
                
                if(getEventType(event1) == MOUSE_CLICKED)
                {
                   continue;
                }
           }
        }
        //Left Collision
        else if(getY(ball) <= 0)
        {
            velocityy = -velocityy;
            
        }
        
        GObject object = detectCollision(window, ball);
       
        if(object != NULL)
        {
         
            if (object == paddle)
            {
            
                velocityy = -velocityy;
            
            }
            if (strcmp(getType(object), "GRect") == 0 && object != paddle)
            {
                removeGWindow(window, object);  
                velocityy = -velocityy; 
                points = points + 1;
                bricks = bricks -1;
                updateScoreboard(window,label,points);
            }
        }
        
         
        
        
        
       
        
    }

    // wait for click before exiting
    waitForClick();

    // game over
    closeGWindow(window);
    return 0;
}

/**
 * Initializes window with a grid of bricks.
 */
void initBricks(GWindow window)
{
   
      
    int pixver = 50;  //  for vertical bricks
    
    for(int i = 0; i < ROWS; i++)
    {
        int pixhor = 2;   // Initial pixel for bricks
        for(int j = 0; j < COLS; j++)
        {
            GRect rect = newGRect(pixhor,pixver,36,10);
            setFilled(rect, true);
            setColor(rect, "RED");
            add(window,rect);
            pixhor = pixhor + 40;
            
        }
        
        pixver = pixver + 14;
    }
}

/**
 * Instantiates ball in center of window.  Returns ball.
 */
GOval initBall(GWindow window)
{
    GOval oval = newGOval(180,280,2*RADIUS,2*RADIUS);
    setFilled(oval, true);
    setColor(oval, "Black");
    add(window, oval);
    return oval;
}

/**
 * Instantiates paddle in bottom-middle of window.
 */
GRect initPaddle(GWindow window)
{
    GRect rect = newGRect(165,550,70,10);
    setFilled(rect, true);
    setColor(rect, "BLACK");
    add(window, rect);
    return rect;
}

/**
 * Instantiates, configures, and returns label for scoreboard.
 */
GLabel initScoreboard(GWindow window)
{

    GLabel label = newGLabel("0");
    setFont(label, "SansSerif-36");
    double x = (getWidth(window) - getWidth(label)) / 2;
    double y = (getHeight(window) + getFontAscent(label)) / 2;
    
    setLocation(label, x, y);
    add(window,label);
    return label;
}

/**
 * Updates scoreboard's label, keeping it centered in window.
 */
void updateScoreboard(GWindow window, GLabel label, int points)
{
    // update label
    char s[12];
    sprintf(s, "%i", points);
    setLabel(label, s);

    // center label in window
    double x = (getWidth(window) - getWidth(label)) / 2;
    double y = (getHeight(window) - getHeight(label)) / 2;
    setLocation(label, x, y);
}

/**
 * Detects whether ball has collided with some object in window
 * by checking the four corners of its bounding box (which are
 * outside the ball's GOval, and so the ball can't collide with
 * itself).  Returns object if so, else NULL.
 */
GObject detectCollision(GWindow window, GOval ball)
{
    // ball's location
    double x = getX(ball);
    double y = getY(ball);

    // for checking for collisions
    GObject object;

    // check for collision at ball's top-left corner
    object = getGObjectAt(window, x, y);
    if (object != NULL)
    {
        return object;
    }

    // check for collision at ball's top-right corner
    object = getGObjectAt(window, x + 2 * RADIUS, y);
    if (object != NULL)
    {
        return object;
    }

    // check for collision at ball's bottom-left corner
    object = getGObjectAt(window, x, y + 2 * RADIUS);
    if (object != NULL)
    {
        return object;
    }

    // check for collision at ball's bottom-right corner
    object = getGObjectAt(window, x + 2 * RADIUS, y + 2 * RADIUS);
    if (object != NULL)
    {
        return object;
    }

    // no collision
    return NULL;
}