//
//  DetailViewController.m
//  DealzFrontEnd2
//
//  Created by David O'Regan on 22/03/2014.
//  Copyright (c) 2014 David O'Regan. All rights reserved.
//

#import "DetailViewController.h"

@interface DetailViewController ()

@end

@implementation DetailViewController

@synthesize CarNameLabel, CarLinkLabel, CarPriceLabel, CarYearLabel, CarLocationLabel, CarMileageLabel, CarEngineLabel, currentCar;

- (id)initWithNibName:(NSString *)nibNameOrNil bundle:(NSBundle *)nibBundleOrNil
{
    self = [super initWithNibName:nibNameOrNil bundle:nibBundleOrNil];
    if (self) {
        // Custom initialization
    }
    return self;
}

- (void)viewDidLoad
{
    [super viewDidLoad];
    // Do any additional setup after loading the view.
    
    //Loads label method
    [self setLabels];
}

- (void)didReceiveMemoryWarning
{
    [super didReceiveMemoryWarning];
    // Dispose of any resources that can be recreated.
}

#pragma mark -
#pragma mark Mathods

-(void)getCar:(id)carObject
{
    currentCar = carObject;
}

-(void)setLabels
{
    CarNameLabel.text = currentCar.title;
    CarLinkLabel.text = currentCar.link;
    CarYearLabel.text = currentCar.carYear;
    CarPriceLabel.text = currentCar.price;
    CarLocationLabel.text = currentCar.location;
    CarMileageLabel.text = currentCar.mileage;
    CarEngineLabel.text = currentCar.engine;


}

@end
