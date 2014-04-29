//
//  DetailViewController.h
//  DealzFrontEnd2
//
//  Created by David O'Regan on 22/03/2014.
//  Copyright (c) 2014 David O'Regan. All rights reserved.
//

#import <UIKit/UIKit.h>
#import "Cars.h"


@interface DetailViewController : UIViewController

@property(nonatomic,strong) IBOutlet UILabel * CarNameLabel;
@property(nonatomic,strong) IBOutlet UILabel * CarLinkLabel;
@property(nonatomic,strong) IBOutlet UILabel * CarPriceLabel;
@property(nonatomic,strong) IBOutlet UILabel * CarYearLabel;
@property(nonatomic,strong) IBOutlet UILabel * CarLocationLabel;
@property(nonatomic,strong) IBOutlet UILabel * CarMileageLabel;
@property(nonatomic,strong) IBOutlet UILabel * CarEngineLabel;

@property(nonatomic, strong) Cars * currentCar;

#pragma mark -
#pragma mark Methods

-(void)getCar:(id)carObject;
-(void)setLabels;



@end
