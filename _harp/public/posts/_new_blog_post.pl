#!/usr/bin/env perl
use strict;
use warnings;
use JSON;
use String::Util 'trim';

open(my $fh, '<', '_data.json') || die "Couldn't open '_data.json' for reading: ".$!;

my $json_text = "";

while(!eof $fh) {
  my $line = <$fh>;
  chomp $line;
  $json_text = $json_text . trim( $line );
}

my $blog_data = decode_json( $json_text );

my $blog_data_size = scalar keys %$blog_data;

my $new_post_id = sprintf("%04d", $blog_data_size);



my $js = JSON::PP->new->pretty;

my $sorter = sub {
  my ($json_obj, $undefined) = @_;

  my $is_hash = ref $json_obj->{$JSON::PP::a} eq "HASH";

  my $is_id = 0;

  if ($is_hash) {
    $is_id = exists $json_obj->{$JSON::PP::a}->{"id"} && defined $json_obj->{$JSON::PP::a}->{"id"};
  }

  return $json_obj->{$JSON::PP::b}->{"id"} cmp $json_obj->{$JSON::PP::a}->{"id"}
    if $is_id;

  return $JSON::PP::a cmp $JSON::PP::b;
};

$json_text = $js->sort_by($sorter)->encode($blog_data);

print $json_text;