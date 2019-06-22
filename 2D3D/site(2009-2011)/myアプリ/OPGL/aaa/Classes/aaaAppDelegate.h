//
//  aaaAppDelegate.h
//  aaa
//
//  Created by 会田 誠 on 11/04/30.
//  Copyright 2011 __MyCompanyName__. All rights reserved.
//

#import <UIKit/UIKit.h>

@class aaaViewController;

@interface aaaAppDelegate : NSObject <UIApplicationDelegate> {
    UIWindow *window;
    aaaViewController *viewController;
}

@property (nonatomic, retain) IBOutlet UIWindow *window;
@property (nonatomic, retain) IBOutlet aaaViewController *viewController;

@end

