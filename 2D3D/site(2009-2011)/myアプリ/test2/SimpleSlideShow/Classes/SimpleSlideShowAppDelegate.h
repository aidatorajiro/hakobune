//
//  SimpleSlideShowAppDelegate.h
//  SimpleSlideShow
//
//  Created by 会田 誠 on 11/04/30.
//  Copyright 2011 __MyCompanyName__. All rights reserved.
//

#import <UIKit/UIKit.h>

@interface SimpleSlideShowAppDelegate : NSObject <UIApplicationDelegate,UIPickerViewDelegate,UIPickerViewDataSource> {
    UIWindow *window;
	UIImageView *mainImage;
	UIButton *showButton;
	UIPickerView *imagePicker;
	NSArray *imageArray;
}

@property (nonatomic, retain) IBOutlet UIWindow *window;
@property (nonatomic, retain) IBOutlet UIImageView *mainImage;
@property (nonatomic, retain) IBOutlet UIButton *showButton;
@property (nonatomic, retain) IBOutlet UIPickerView *imagePicker;
- (IBAction) showImage;
- (IBAction) hidePicker;

@end

