//
//  HyundaiViewController.h
//  DealzFrontEnd2
//
//  Created by David O'Regan on 18/03/2014.
//  Copyright (c) 2014 David O'Regan. All rights reserved.
//

#import <UIKit/UIKit.h>

@interface HyundaiViewController : UITableViewController

@property (nonatomic, strong) NSMutableArray * jsonArray;
@property (nonatomic, strong) NSMutableArray * carArray;

#pragma mark -
#pragma mark Class Methods
-(void) retriveData;


@end
