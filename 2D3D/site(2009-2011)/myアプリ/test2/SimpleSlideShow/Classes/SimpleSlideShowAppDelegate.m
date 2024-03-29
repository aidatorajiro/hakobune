//
//  SimpleSlideShowAppDelegate.m
//  SimpleSlideShow
//
//  Created by 会田 誠 on 11/04/30.
//  Copyright 2011 __MyCompanyName__. All rights reserved.
//

#import "SimpleSlideShowAppDelegate.h"

@implementation SimpleSlideShowAppDelegate

@synthesize window;

@synthesize mainImage;

@synthesize showButton;

@synthesize imagePicker;
#pragma mark -
#pragma mark Application lifecycle

- (BOOL)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions {    
    
    // Override point for customization after application launch.
    
    [self.window makeKeyAndVisible];
    //mainImage.image = [UIImage imageNamed:@"sample.jpg"];
	imageArray = [[NSArray arrayWithObjects:@"sample.jpg",@"sample2.jpg",@"sample3.jpg",nil]retain];
    return YES;
}
- (void)applicationWillResignActive:(UIApplication *)application {
    /*
     Sent when the application is about to move from active to inactive state. This can occur for certain types of temporary interruptions (such as an incoming phone call or SMS message) or when the user quits the application and it begins the transition to the background state.
     Use this method to pause ongoing tasks, disable timers, and throttle down OpenGL ES frame rates. Games should use this method to pause the game.
     */
}


- (void)applicationDidEnterBackground:(UIApplication *)application {
    /*
     Use this method to release shared resources, save user data, invalidate timers, and store enough application state information to restore your application to its current state in case it is terminated later. 
     If your application supports background execution, called instead of applicationWillTerminate: when the user quits.
     */
}


- (void)applicationWillEnterForeground:(UIApplication *)application {
    /*
     Called as part of  transition from the background to the inactive state: here you can undo many of the changes made on entering the background.
     */
}


- (void)applicationDidBecomeActive:(UIApplication *)application {
    /*
     Restart any tasks that were paused (or not yet started) while the application was inactive. If the application was previously in the background, optionally refresh the user interface.
     */
}


- (void)applicationWillTerminate:(UIApplication *)application {
    /*
     Called when the application is about to terminate.
     See also applicationDidEnterBackground:.
     */
}


#pragma mark -
#pragma mark Memory management

- (void)applicationDidReceiveMemoryWarning:(UIApplication *)application {
    /*
     Free up as much memory as possible by purging cached data objects that can be recreated (or reloaded from disk) later.
     */
}

- (void)showImage{
	mainImage.image = [UIImage imageNamed:@"sample.jpg"];
}
- (NSInteger)numberOfComponentsInPickerView:(UIPickerView *)pickerView{
	return 1;
}
- (NSInteger)pickerView:(UIPickerView *)pickerView numberOfRowsInComponent:(NSInteger)component{
	return 3;
}
- (NSString *)pickerView:(UIPickerView *)pickerView titleForRow:(NSInteger)row forComponent:(NSInteger)component{
	return [imageArray objectAtIndex:row];
}
- (void) pickerView:(UIPickerView *)pickerView didSelectRow:(NSInteger)row inComponent:(NSInteger)component{
	mainImage.image = [UIImage imageNamed:[imageArray objectAtIndex:row]];
}
- (void)hidePicker {
	if (imagePicker.alpha == 1.0f) {
		imagePicker.alpha = 0.0f;
		[showButton setTitle:@"show Picker" forState:UIControlStateNormal];
	}else{
		imagePicker.alpha = 1.0f;
		[showButton setTitle:@"Hide picker" forState:UIControlStateNormal];
	}
}
- (void)dealloc {
	[mainImage release];
	[showButton release];
	[imagePicker release];
	[imageArray release];
    [window release];
    [super dealloc];
}


@end
